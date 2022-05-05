from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.Pedometer import Pedometer
from matplotlib import pyplot as plt
from time import time
import numpy as np
import time as t

if __name__ == "__main__":
  fs = 50                         # sampling rate
  num_samples = 250               # 5 seconds of data @ 50Hz
  process_time = 1                # compute the step count every second

  ped = Pedometer(num_samples, fs, [])

  comms = Communication('COM4', 115200)
  comms.clear()                   # just in case any junk is in the pipes
  comms.send_message("wearable")  # begin sending data

  try:
    previous_time = time()
    while(True):
      message = comms.receive_message()
      if message != None and "steps" in message:
        print(message)
      if(message != None):
        try:
          (m1, m2, m3, m4) = message.split(',')
        except ValueError:        # if corrupted data, skip the sample
          continue

        # Collect data in the pedometer
        ped.add(int(m2),int(m3),int(m4))

        # if enough time has elapsed, process the data and plot it
        current_time = time()

        try:
          comms.send_message(strsteps)
        except:
          pass

        if (current_time - previous_time > process_time):
          previous_time = current_time

          steps, peaks, filtered = ped.process()
          print("Step count: {:d}".format(steps))
          strsteps = str(steps)

          comms.send_message(strsteps)

          plt.cla()
          plt.plot(filtered)
          plt.title("Step Count: %d" % steps)
          plt.show(block=False)
          plt.pause(0.001)
          last_str = strsteps

  except(Exception, KeyboardInterrupt) as e:
    print(e)                     # Exiting the program due to exception
  finally:
    print("Closing connection.")
    comms.send_message("sleep")  # stop sending data
    comms.close()