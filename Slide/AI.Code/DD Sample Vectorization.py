import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
data = genfromtxt('data.csv', delimiter=',')
areas = data[:,0]
prices = data[:,1:]
N = areas.size
# vector [x, b]
data = np.c_[areas, np.ones((N, 1))]
print(data )
print("data:\n", data.shape)
theta = np.array([[-0.34], [0.04]])  # [w, b]
print("theta:\n", theta.shape)
# params
lr = 0.01
epoch_max = 10
mini_bath = 2
losses = []  # for debug
for epoch in range(epoch_max):
    for i in range(0, N, mini_bath):
        # get m samples
        x = data[i:i + mini_bath, :]
        y = prices[i:i + mini_bath, :]

        # predict y_hat
        y_hat = x.dot(theta)

        # compute loss
        loss = np.multiply((y_hat - y), (y_hat - y))
        losses.append(np.mean(loss))

        # compute gradient
        k = 2 * (y_hat - y)
        gradients = np.multiply(x, np.hstack([k, k]))
        gradients = np.ones((1, mini_bath)).dot(gradients) / mini_bath

        # update weights
        theta = theta - lr * gradients.T

plt.plot(losses)
plt.xlabel('iteration')
plt.ylabel('losses')
plt.show()
