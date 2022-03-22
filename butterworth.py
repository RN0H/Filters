import scipy
from scipy import signal
import numpy as np
import random
import matplotlib.pyplot as plt


class Filter:
    def __init__ (self,**args):
        self.__dict__.update(args)
        self.nyq = self.Sampling_frequency/2
        self.Low_frequency_cutoff/=self.nyq;
        self.High_frequency_cutoff/=self.nyq

    def butterlow(self, data):
        d, n = signal.butter(self.order, self.Low_frequency_cutoff, btype="lowpass")
        self.filtered_data = signal.filtfilt(d,n, data)
        return self.filtered_data

    def butterhigh(self, data):
        d, n = signal.butter(self.order, self.High_frequency_cutoff, btype="highpass")
        self.filtered_data = signal.filtfilt(d,n, data)
        return self.filtered_data

if __name__ == "__main__":
    configs = {"Sampling_frequency":1000,
            "Low_frequency_cutoff":10,
            "High_frequency_cutoff":20,
            "order":2
            }
    y =  [np.random.randn() for _ in range(1000)]
    yf = Filter(**configs).butterlow(y)

    plt.xlabel("Time(s)"); plt.ylabel("points")
    plt.xlim([0,1000]); plt.ylim([-10, 10])


    plt.plot(range(len(y)), y, 'r', range(len(yf)), yf, 'g')
    plt.legend(["signal", "filtered"], loc = "upper right")
    plt.show()
