import numpy
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from ECE16Lib.HRMonitor import HRMonitor
import os

ground_truth = np.array([80,75,79,58,58])# reference heart rates
estimates = np.zeros((5), dtype=int) # estimated heart rates from your algorithm
#enter your pid so that it can find your correct directory
pid = "a14588777"

def load_data(filename):
  return np.genfromtxt(filename, delimiter=",")
def estimate_sampling_rate(times):
  return 1 / np.mean(np.diff(times))
def eval_hr_monitor():
  directory = "./data/" + pid
  i=0
  for filename in os.scandir(directory):
    # Load the data,
    data = load_data(filename)
    # Data is 500x2 containing the time, ppg samples
    t = data[:, 0]
    t = (t - t[0]) / 1e3  # make time range from 0-10 in seconds
    ppg = data[:, 1]

    # Estimate the sampling rate based on time samples
    fs = estimate_sampling_rate(t)
    #print("Estimated sampling rate: {:.2f} Hz".format(fs))

    hr_monitor = HRMonitor(500, 50)
    hr_monitor.add(t, ppg)

    hr, peaks, filtered = hr_monitor.process()
    estimates[i] = int(hr)

    i+=1

eval_hr_monitor()
print("Our estimates read: ", + estimates)
print("Our ground truth reads: ", + ground_truth)

ground_truth = np.array([63, 56, 96, 79, 63, 120, 152, 111, 95, 57])
estimates =    np.array([65, 54, 96, 71, 63, 127, 159, 115, 104, 54])
[R,p] = stats.pearsonr(ground_truth, estimates) # correlation coefficient

plt.figure(1)
plt.clf()

# Correlation Plot
plt.subplot(211)
plt.plot(estimates, estimates)
plt.scatter(ground_truth, estimates)

plt.ylabel("Estimated HR (BPM)")
plt.xlabel("Reference HR (BPM)")
plt.title("Correlation Plot: Coefficient (R) = {:.2f}".format(R))

# Bland-Altman Plot
avg = np.mean( np.array([estimates, ground_truth]), axis=0 )# take the average between each element of the ground_truth and
      # estimates arrays and you should end up with another array
dif = ground_truth - estimates # take the difference between ground_truth and estimates
std = np.std(dif)# get the standard deviation of the difference (using np.std)
bias = np.mean(dif)# get the mean value of the difference
upper_std = bias + 1.96*std# the bias plus 1.96 times the std
lower_std = bias - 1.96*std# the bias minus 1.96 times the std

plt.subplot(212)
plt.scatter(avg, dif)

plt.plot(avg, len(avg)*[bias])
plt.plot(avg, len(avg)*[upper_std])
plt.plot(avg, len(avg)*[lower_std])

plt.legend(["Mean Value: {:.2f}".format(bias),
  "Upper bound (+1.96*STD): {:.2f}".format(upper_std),
  "Lower bound (-1.96*STD): {:.2f}".format(lower_std)
])

plt.ylabel("Difference between estimates and ground_truth (BPM)")
plt.xlabel("Average of estimates and ground_truth (BPM)")
plt.title("Bland-Altman Plot")
plt.show()