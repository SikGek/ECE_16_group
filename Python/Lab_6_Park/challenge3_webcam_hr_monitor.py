from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.HRMonitor import HRMonitor
import os
from matplotlib import pyplot as plt
import numpy as np
from time import time, time_ns
import cv2


if __name__ == "__main__":

    fs = 50                         # sampling rate of 50Hz
    num_samples = 3000               # 10 seconds of data @ 50Hz
    refresh_time = 1                # compute the heart rate every second
    heartppg = 0                    # this is where we will store our heart rate data from arduino
    timeppg = 0                     # this is where we will store our time data from arduino
    begin_tim = time_ns()
    begin_tim = begin_tim/1000000000

    #initiliaze our circularlists to hold heart rate and time data
    ppg = [CircularList([], num_samples)]
    times = CircularList([], num_samples)

    #initliaze connection to arduino
    comms = Communication('COM4', 115200)
    comms.clear()                   # just in case any junk is in the pipes
    comms.send_message("wearable")  # begin sending data
    # create our hearmonitor object
    heart = HRMonitor(num_samples, fs, [])
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    try:
        previous_time = time()
        while(True):
            #receive message from the arduino
            message = comms.receive_message()
            _, frame = cap.read() 
            try:
                #receive the raw data from arduino
                #(timeppg, heartppg) = message.split(',')
                new_sample = frame.mean(axis=0).mean(axis=0)
                #print(new_sample)
                new_sample = new_sample[2] # replace the ? with index of the RED channel
                tim = time_ns()
                tim = tim/1000000000
                tim = tim - begin_tim
            except ValueError:
                continue
            #add our data to circular list
            ppg.add(int(new_sample))
            times.add(int(tim))
            # update our OLED with current heart rate once a second
            current_time = time()
            #print(current_time - previous_time)
            if (current_time - previous_time > refresh_time):
                previous_time = current_time
                #update our heart rate object with our listed data
                heart.add(times,ppg)
                try:                 
                    #filter and process our data
                    hr, peaks, filtered =  heart.process()
                    #print(1)
                    #heart rate needs to be an int and scaled up
                    #hr = int(hr*1000)
                    output = int(hr)
                    print(output, times[-1])
                    # if our hr is too high or low than the watch is not attached. or they dead
                    if (hr > 250 or hr < 20):
                        output = "N/A"
                    print("Your heart rate is currently: ", output)
                    #send heart rate data to arduino
                    
                except:
                    continue
            cv2.imshow('Input', frame)
            c = cv2.waitKey(1)
            if c == 27:
                break
    except(KeyboardInterrupt) as e:
        print(e)
    finally:
        plt.plot(times, filtered)
        
        plt.title("Estimated Heart Rate: {:.2f} bpm".format(hr))
        #plt.plot(times[peaks], filtered[peaks], 'rx')
        #plt.plot(times, [0.6]*len(filtered), "b--")
        plt.show()
        plt.plot(times, ppg)
        plt.show()
        comms.send_message(str(output))
        print("Closing connection. ")
        cap.release()
        comms.send_message("sleep")
        comms.close()