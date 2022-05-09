Ihyun Park A16605545
William Lynch A14588777

Tutorial 1:

In this tutorial, we learned how to send sample data from the accelerometer on the arduino and collect it in our python code. With this sample data we computed the L1 norm of it, which is the sum of the absolute value of data in their respective axis and plotted it. After we plotted it, we were able to see peaks where we took steps and saved the numerical data to a .csv file for future reference.

Tutorial 2:


Tutorial 3:

In this tutorial, we learned how to make the pedometer class from scratch. Using the samples we obtained from the arduino, we pass it into the pedometer class, where we filter the signal to make it smooth using the filtering process we learned in the DSP tutorial. After initializing the values, we created a function for calculating the L1 norm and add it to an array. After that, we grab new samples from the norm array, and filter it. We personally detrended, put it through a low pass filter, calculated the gradient, then calculated the moving average.