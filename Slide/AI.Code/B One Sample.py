import numpy as np
from numpy import genfromtxt
# pick data
data = genfromtxt('data.csv', delimiter=',')
areas = data[:, 0]
prices = data[:, 1]
N = areas.size
# get x bar
X_bar = np.c_[areas, np.ones((N, 1))]
# init theta (w,b)
theta = np.array([-0.34, 0.04])

# param
lr = 0.01
max_epoch = 10
losses = []
# get sample
for _ in range(max_epoch):
    for i in range(N):
        x = X_bar[i]
        y = prices[i:i+1]
        # predict y_hat
        y_hat = x.dot(theta)
        # compute loss
        loss = (y_hat - y)*(y_hat - y)
        losses.append(loss)
        # compute gradient
        d_theta = 2*x*(y_hat-y)
        # update weight
        theta = theta - lr * d_theta

print("theta:\n", theta)
print("losses=\n", losses[-1])


import matplotlib.pyplot as plt
plt.plot(losses) # test with losses[3:]
plt.xlabel('iteration')
plt.ylabel('losses')
plt.show()

x_data = range(2, 8)
y_data = [x*theta[0] + theta[1] for x in x_data]
plt.plot(x_data, y_data)
plt.scatter(areas, prices)
plt.xlabel('Diện tích nhà')
plt.ylabel('Giá nhà ')

plt.xlim(3, 7)
plt.ylim(4, 10)
plt.show()