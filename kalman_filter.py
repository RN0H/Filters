import matplotlib.pyplot as plt
import numpy as np
import random

class KF:

    def __init__(self, X, P):
        self.X = X
        self.P = P
        self.U = 0

    def predict(self):
        F = 1; G = 0
        Q = 0.01

        self.X_ = F*self.X   + G*self.U
        self.P_ = F*self.P*F + Q

    def update(self, measurement):
        H = 1; M = 1
        V = 0.01; R = 0.1
        Z = measurement

        #INNOVATION
        y = Z - H*self.X
        S = H*self.P_*H + R

        #KALMAN GAIN
        K = (self.P_*H)/(S)

        #STATE UPDATE
        self.X = self.X_ + K*(y)

        #UPDATE COVARIANCE
        self.P = (1 - K*H)*self.P_




if __name__=="__main__":
        plt.ion()
        fig = plt.figure()
        plt.xlim([0, 50])
        x,y, yk = [], [], []

        k = KF(0, 1)
        for _ in range(100):
            x.append(_)
            plt.ylim([-20,20])
            if _>50:
                plt.xlim([50, 100])
            sense = np.random.randn()
            y.append(sense)

            k.predict()         #prediction step
            k.update(sense)     #update using measurement

            yk.append(k.X)
            plt.plot(x,y, 'r', x, yk, 'g')
            plt.legend(["Signal", "Filterd"])
            plt.show()
            plt.pause(0.1)