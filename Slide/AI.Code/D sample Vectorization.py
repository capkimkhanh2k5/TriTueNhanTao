
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

data = genfromtxt('data.csv', delimiter=',')
areas = data[:,0]
prices = data[:,1:]
N = areas.size

# vector [x, b]
data = np.c_[areas, np.ones((N, 1))]
data = data.T


theta = np.array([[-0.34], [0.04]])  # [w, b]T

# params
lr = 0.01
epoch_max = 10
bath_mini = 2
losses = []  # for debug
for epoch in range(epoch_max):
    for i in range(0, N, bath_mini):
        # get bath_mini samples
        x = data[:, i:i + bath_mini]
        y = prices[i:i + bath_mini, :]

        # predict y_hat
        y_hat = theta.T.dot(x)

        # compute loss
        loss = np.multiply((y_hat - y.T), (y_hat - y.T))
        losses.append(np.mean(loss))

        # compute gradient
        k = 2 * (y_hat - y.T)
        gradients = np.multiply(x, np.vstack((k, k)))
        gradients = gradients.dot(np.ones((bath_mini, 1))) / bath_mini

        # update weights
        theta = theta - lr * gradients


plt.plot(losses)
plt.xlabel('iteration')
plt.ylabel('losses')
plt.show()

