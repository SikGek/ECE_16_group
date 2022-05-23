from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.HRMonitor import HRMonitor
from ECE16lib.Pedometer import Pedometer
import pyowm
from pyowm import OWM
import os
from matplotlib import pyplot as plt
import numpy as np
from time import time


if __name__ == "__main__":


    process_time = 1  # compute the step count every second

    ped = Pedometer(num_samples, fs, [])

    strsteps = '0'
    strjumps = '0'

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
    while(True):
        message = comms.recieve_message()

        # if we receive weather from the arduino we want to display the weather and time
        if (message == "Weather"):
            owm = OWM('4f1f4c6040e4ec94f3809aaba5c6f914').weather_manager()
            weather = owm.weather_at_place('San Diego,CA,US').weather
            print(weather.temperature('fahrenheit'))
            dt = datetime.datetime.now()
            # w = weather.get_weather()
            temp = weather.temperature('fahrenheit')

            while (message == "Weather"):
                send_message(ser, "Date:")
                time.sleep(2)
                send_message(ser, dt.strftime("%x\n"))
                time.sleep(2)
                send_message(ser, "Time:")
                time.sleep(2)
                send_message(ser, dt.strftime("%X\n"))
                time.sleep(2)
                send_message(ser, "Temperature: ")
                time.sleep(2)
                send_message(ser, str(list(temp.items())[0]))
                time.sleep(2)
                message = receive_message(ser)
                print(message)
        # if we receive heart from the arduino we want to start processing the heart information and displaying
        if (message == "Heart"):
            try:
                previous_time = time()
                while(message != "Steps"):
                    #receive message from the arduino
                    message = comms.receive_message()
                    # WE NEED TO PARSE EACH HEART OUT, INSERT THAT HERE
                    print(message)
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

        if (message == "Steps"):
            try:
                previous_time = time()
                while (message != "Weather"):
                    message = comms.receive_message()
                    # WE NEED TO PARSE EACH STEPS OUT, INSERT THAT HERE
                    print(message)
                    if (message != None):
                        try:
                            (m1, m2, m3, m4) = message.split(',')
                        except ValueError:  # if corrupted data, skip the sample
                            continue
                        # print(1)
                        # Collect data in the pedometer
                        ped.add(int(m2), int(m3), int(m4))

                        # if enough time has elapsed, process the data and plot it
                        current_time = time()

                        # if data is available to send, send data
                        try:
                            comms.send_message(strsteps)
                        except:
                            pass
                        # print(1)
                        if (current_time - previous_time > process_time):
                            previous_time = current_time

                            steps, f, peaks, filtered = ped.process()

                            steps, peaks, filtered = ped.process()
                            print("Step count: {:d}".format(steps))
                            strsteps = str(steps)

                            comms.send_message(strsteps)
                            # print(1)
                            plt.cla()
                            plt.plot(filtered)
                            plt.title("Step Count: %d" % steps)
                            plt.show(block=False)
                            plt.pause(0.001)
                            last_str = strsteps

            except(Exception, KeyboardInterrupt) as e:
                print(e)  # Exiting the program due to exception



        print("Closing connection. ")
        comms.send_message("sleep")
        comms.close()