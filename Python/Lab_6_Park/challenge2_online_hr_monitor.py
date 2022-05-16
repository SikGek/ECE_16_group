from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.HRMonitor import HRMonitor
import os
from matplotlib import pyplot as plt
import numpy as np
from time import time


if __name__ == "__main__":

    fs = 50                         # sampling rate of 50Hz
    num_samples = 500               # 10 seconds of data @ 50Hz
    refresh_time = 1                # compute the heart rate every second
    heartppg = 0                    # this is where we will store our heart rate data from arduino
    timeppg = 0                     # this is where we will store our time data from arduino

    #initiliaze our circularlists to hold heart rate and time data
    ppg = CircularList([], num_samples)
    times = CircularList([], num_samples)

    #initliaze connection to arduino
    comms = Communication('COM4', 115200)
    comms.clear()                   # just in case any junk is in the pipes
    comms.send_message("wearable")  # begin sending data
    # create our hearmonitor object
    heart = HRMonitor(num_samples, fs, [])

    try:
        previous_time = time()
        while(True):
            #receive message from the arduino
            message = comms.receive_message()
            if(message != None):
                try:
                    #receive the raw data from arduino
                    (timeppg, heartppg) = message.split(',')
                except ValueError:
                    continue
                #add our data to circular list
                ppg.add(int(heartppg))
                times.add(int(timeppg))

                # update our OLED with current heart rate once a second
                current_time = time()
                if (current_time - previous_time > refresh_time):
                    previous_time = current_time
                    #update our heart rate object with our listed data
                    heart.add(times,ppg)
                    try:
                        #filter and process our data
                        hr, peaks, filtered =  heart.process()
                        #heart rate needs to be an int and scaled up
                        hr = int(hr*1000)
                        output = hr
                        # if our hr is too high or low than the watch is not attached. or they dead
                        if (hr > 250 or hr < 20):
                            output = "N/A"
                        print("Your heart rate is currently: ", output)
                        #send heart rate data to arduino
                        comms.send_message(str(output))
                    except:
                        continue
    except(KeyboardInterrupt) as e:
        print(e)
    finally:
        print("Closing connection. ")
        comms.send_message("sleep")
        comms.close()