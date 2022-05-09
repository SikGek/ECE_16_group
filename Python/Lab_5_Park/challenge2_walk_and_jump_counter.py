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

  comms = Communication('COM5', 115200)
  comms.clear()                   # just in case any junk is in the pipes
  comms.send_message("wearable")  # begin sending data

  try:
    previous_time = time()
    while(True):
      # here we receive the upload message and we build out our circular lists
      message = comms.receive_message()
      if(message != None):
        print(message)
      if(message == "uploadData"):
        print(message)
        current_time = time()
        while(message != "uploadComplete"):
          #our data is already being uploaded entry by entry.
          try:
            message = comms.receive_message()
            (m1, m2, m3, m4) = message.split(',')
          except ValueError:
            continue
          # Collect data in the pedometer
          ped.add(int(m2),int(m3),int(m4))

      # if enough time has elapsed, process the data and plot it
      current_time = time()
      # if we receive a request for jumps and steps, lets send it
      message = comms.receive_message()
      if (message == 'stepRequest'):
        comms.send_message(strsteps)
      if (message == 'jumpRequest'):
        comms.send_message(strjumps)
      if (current_time - previous_time > process_time):
        previous_time = current_time

        steps, jumps, peaks, filtered = ped.process()
        print("Step count: {:d}".format(steps))
        strsteps = str(steps)
        strjumps = str(jumps)

        comms.send_message(strsteps)

        plt.cla()
        plt.plot(filtered)
        plt.title("Step Count: %d" % steps)
        plt.show(block=False)
        plt.pause(0.001)
        # last_str = strsteps

  except(Exception, KeyboardInterrupt) as e:
    print(e)                     # Exiting the program due to exception
  finally:
    print("Closing connection.")
    comms.send_message("sleep")  # stop sending data
    comms.close()