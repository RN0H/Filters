import matplotlib.pyplot as plt
import numpy as np
import random

class KF:

    def __init__(self, X, P):
        self.X = X
        self.P = P
        self.U = 0

    def predict(self, *new_state):
        F = 1; G = 0    #F = state dynamic matrix, G = control input matrix
        Q = 0.1         #Q = process covariance
        if new_state:   self.X = new_state[0]
        self.X_ = F*self.X   + G*self.U
        self.P_ = F*self.P*F + Q

    def update(self, measurement):
        H = 1; M = 1
        V = 0.1; R = 0.1
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
            sense = 10*np.random.randn()
            y.append(sense)

            k.predict(sense)                      #prediction step = real
            k.update(sense+5*np.random.randn())   #update using measurement = real+noise

            yk.append(k.X)
            plt.plot(x,y, 'r', x, yk, 'g')
            plt.legend(["Signal", "KF"])
            plt.show()
            plt.pause(0.1)