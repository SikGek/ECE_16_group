Ihyun Park A16605545
William Lynch A14588777

Tutorial 1:

![t1_img](images/Peaks.png)

In this tutorial, we learned how to send sample data from the accelerometer on the arduino and collect it in our python code. With this sample data we computed the L1 norm of it, which is the sum of the absolute value of data in their respective axis and plotted it. After we plotted it, we were able to see peaks where we took steps and saved the numerical data to a .csv file for future reference.

Tutorial 2:

When I set the window size to the size of data, I did not observe any noticeable differences.

The noise could be due to the small fluctuations in the raw data that gets captured as change in value when derived.

If the sampling rate was 120 Hz, the Nyquist frequency would be 60 Hz. If signal bandwidth is composed from 0-10 Hz, the minimum sampling rate will be 20 Hz. Since we should be doubling the maximum frequency.

In this tutorial, we learned about Digital Signal Processing and filtering. We discussed different methods to smooth out or improve the values of the data, starting with calculating the L1 norm of the data with different axis, moving average filter to remove noise, deterending it to zero it out, finding the gradient to define peaks, power signal density, low and high pass filtering to filter out signals outside of a certain threshold of bandwidths, and counting peaks depending on the thresholds. Then we put all of this into a module so that we could use it in other files with ease.
Tutorial 3:

In this tutorial, we learned how to make the pedometer class from scratch. Using the samples we obtained from the arduino, we pass it into the pedometer class, where we filter the signal to make it smooth using the filtering process we learned in the DSP tutorial. After initializing the values, we created a function for calculating the L1 norm and add it to an array. After that, we grab new samples from the norm array, and filter it. We personally detrended, put it through a low pass filter, calculated the gradient, then calculated the moving average. Then, we selected the appropriate threshold values for it to be able to detect steps correctly. Finally, we tested the class out with the provided data and also with data from our arduino.

Challenge 1:

Challenge 2:

https://youtu.be/tLGgFZR2EPY

For our algorithm, we stored each data we obtain from the accelerometer into a 1500 long array in arduino, then when the button is pressed, using a for loop we iterate through all of the arrays and send data 1 by 1, which we calculate the norm of it and store it into an array in python. Then we filter that array using different thresholds and store it into different variables for us to send print out and send back to the arduino.