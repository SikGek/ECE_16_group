from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from matplotlib import pyplot as plt
from time import time
import numpy as np

if __name__ == "__main__":
  num_samples = 250               # 2 seconds of data @ 50Hz
  refresh_time = 0.1              # update the plot every 0.1s (10 FPS)

  times = CircularList([], num_samples)
  ax = CircularList([], num_samples)
  ay = CircularList([], num_samples)
  az = CircularList([], num_samples)
  avg_x = CircularList([], num_samples)
  delta_x = CircularList([], num_samples)
  l1 = CircularList([], num_samples)
  l2 = CircularList([], num_samples)
  transformed = CircularList([], num_samples)



  comms = Communication("COM4", 115200)
  comms.clear()                   # just in case any junk is in the pipes
  comms.send_message("wearable")  # begin sending data

  try:
    previous_time = 0
    while(True):
      message = comms.receive_message()
      if(message != None):
        try:
          (m1, m2, m3, m4) = message.split(',')
        except ValueError:        # if corrupted data, skip the sample
          continue


        # add the new values to the circular lists
        times.add(int(m1))
        ax.add(int(m2))
        ay.add(int(m3))
        az.add(int(m4))
        avg_x.add(np.average(ax[-100:]))
        delta_x.add((ax[-2]-ax[-1]))
        l2.add(np.linalg.norm((np.array([ax[-1],ay[-1],az[-1]])), ord = 2))
        l1.add(np.linalg.norm((np.array([ax[-1],ay[-1],az[-1]])), ord = 1))
        transformed.add(np.average(ax[-150:]))

        # if enough time has elapsed, clear the axis, and plot everything
        current_time = time()
        if (current_time - previous_time > refresh_time):
          previous_time = current_time
          plt.clf()
          plt.subplot(421)
          plt.plot(ax)
          plt.subplot(422)
          plt.plot(ay)
          plt.subplot(423)
          plt.plot(az)
          plt.subplot(424)
          plt.plot(avg_x)
          plt.subplot(425)
          plt.plot(delta_x)
          plt.subplot(426)
          plt.plot(l1)
          plt.subplot(427)
          plt.plot(l2)
          plt.subplot(428)
          plt.plot(transformed)
          plt.show(block = False)
          plt.pause(0.001)
  except(Exception, KeyboardInterrupt) as e:
    print(e)                     # Exiting the program due to exception
  finally:
    comms.send_message("sleep")  # stop sending data
    comms.close()