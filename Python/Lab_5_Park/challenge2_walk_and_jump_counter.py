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
  message = ''
  ped = Pedometer(num_samples, fs, [])
<<<<<<< Updated upstream
  strsteps = '0'
  strjumps = '0'
  comms = Communication('COM5', 115200)
=======

  comms = Communication('COM7', 115200)
>>>>>>> Stashed changes
  comms.clear()                   # just in case any junk is in the pipes
  comms.send_message("wearable")  # begin sending data

  try:
    previous_time = time()
    while(True):
      # here we receive the upload message and we build out our circular lists
      message = str(comms.receive_message()).strip()
      message = message.strip()
      # uploadData sent from arduino means the button is pressed and we pull our stored arrays
      if str(message) in "uploadData":
        current_time = time()
        # pull arrays until download is complete
        while(message != "uploadComplete"):
          #our data is already being uploaded entry by entry.
          try:
            # each array is incoming with a newline so strip the line and cast to string
            message = str(comms.receive_message()).strip()
            # split ax,ay,az and sampled toime and store
            (m1, m2, m3, m4) = message.split(',')
          except ValueError:
            continue
          # Collect data in the pedometer
          ped.add(int(m2),int(m3),int(m4))
          current_time = time()
          # Begin process of processing and plotting data
          if (current_time - previous_time > process_time):
            previous_time = current_time
            try:
              # filter data
              steps, jumps, peaks, filtered = ped.process()
              # make counter for steps and jumps
              strsteps = str(steps)
              strjumps = str(jumps)
            except:
              continue
            # lets plot our data and step/jump counter
            plt.cla()
            print(filtered)
            plt.plot(filtered)
            plt.title("Step Count: %d Jump Count: %d" % (steps,jumps))
            plt.show(block=False)
            plt.pause(0.001)

            current_time = time()
      # if we receive a request for jumps and steps, lets send it
      if str(message) in 'stepRequest':
        print("Steps:")
        print(strsteps)
        comms.send_message(strsteps)
      if (message == 'jumpRequest'):
        print("Jumps:")
        print(strjumps)
        comms.send_message(strjumps)


  except(Exception, KeyboardInterrupt) as e:
    print(e)                     # Exiting the program due to exception
  finally:
    print("Closing connection.")
    comms.send_message("sleep")  # stop sending data
    comms.close()