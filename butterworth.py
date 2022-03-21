import scipy
from scipy import signal

configs = {"Sampling_frequency":1000,
            "Low_frequency_cutoff":10,
            "High_frequency_cutoff":20,
            "order":2
            }

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
    pass