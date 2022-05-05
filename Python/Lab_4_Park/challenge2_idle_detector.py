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
        avg_x.add(np.average(ax[-50:]))

        # if enough time has elapsed, clear the axis, and plot everything
        current_time = time()
        if (current_time - previous_time >= 5 and (avg_x[-1] < 1950 or avg_x[-1] > 1750)):
          previous_time = current_time
          comms.send_message("inactive")
        elif (avg_x[-1] > 1950 or avg_x[-1] < 1750):
            previous_time = current_time
            comms.send_message("movement")
  except(Exception, KeyboardInterrupt) as e:
    print(e)                     # Exiting the program due to exception
  finally:
    comms.send_message("sleep")  # stop sending data
    comms.close()