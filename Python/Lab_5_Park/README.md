Ihyun Park A16605545
William Lynch A14588777

Tutorial 1:

In this tutorial, we learned how to send sample data from the accelerometer on the arduino and collect it in our python code. With this sample data we computed the L1 norm of it, which is the sum of the absolute value of data in their respective axis and plotted it. After we plotted it, we were able to see peaks where we took steps and saved the numerical data to a .csv file for future reference.

Tutorial 2:


Tutorial 3:

In this tutorial, we learned how to make the pedometer class from scratch. Using the samples we obtained from the arduino, we pass it into the pedometer class, where we filter the signal to make it smooth using the filtering process we learned in the DSP tutorial. After initializing the values, we created a function for calculating the L1 norm and add it to an array. After that, we grab new samples from the norm array, and filter it. We personally detrended, put it through a low pass filter, calculated the gradient, then calculated the moving average. Then, we selected the appropriate threshold values for it to be able to detect steps correctly. Finally, we tested the class out with the provided data and also with data from our arduino.

Challenge 1:

Challenge 2:

For our algorithm, we stored each data we obtain from the accelerometer into a 1500 long array in arduino, then when the button is pressed, using a for loop we iterate through all of the arrays and send data 1 by 1, which we calculate the norm of it and store it into an array in python. Then we filter that array using different thresholds and store it into different variables for us to send print out and send back to the arduino.