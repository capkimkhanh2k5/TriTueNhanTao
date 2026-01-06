
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
# load data
data = genfromtxt('data.csv', delimiter=',')
areas = data[:, 0]
prices = data[:, 1:]
N = areas.size

# vector [x, b]
data = np.c_[areas, np.ones((N, 1))]
data = data.T
x = data
print("x = ", x.shape)
y = prices  # vector
print(" y= ", y.shape)
theta = np.array([[-0.34], [0.04]]) # vector
# params
n_epochs = 10
lr = 0.01
losses = []  # for debug
for epoch in range(n_epochs):
    # compute output y_hat
    y_hat = theta.T.dot(x)

    # compute loss
    loss = np.multiply((y_hat - y.T), (y_hat - y.T))
    losses.append(np.mean(loss))

    # compute gradient
    b = 2 * (y_hat - prices.T)
    gradient = np.multiply(x, np.vstack((b, b)))
    gradient = gradient.dot(np.ones((N, 1))) / N

    # update weights
    theta = theta - lr * gradient

#plt.plot(losses)
#plt.xlabel('iteration')
#plt.ylabel('losses')
#plt.show()

x_data = range(2, 8)
y_data = [x*theta[0] + theta[1] for x in x_data]
plt.plot(x_data, y_data)
#--------------------------------------
plt.scatter(areas, prices)

plt.xlabel('Diện tích nhà (x 100$m^2$)')
plt.ylabel('Giá nhà (chục lượng vàng)')

plt.xlim(3, 7)
plt.ylim(4, 10)
plt.show()