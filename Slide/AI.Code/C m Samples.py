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
theta = np.array([-0.34, 0.049])

# param
lr = 0.01
batch_size = 2
epoch_max = 10
losses = []
for _ in range(epoch_max):
    for j in range(0, N, batch_size):
        gradients = 0
        sum_loss = 0
        for index in range(j,j+batch_size):
            # pick 2 samples
            xi = X_bar[index]
            yi = prices[index]
            # predict y_hat
            y_hat = xi.dot(theta)
            # compute loss
            li = (y_hat-yi)*(y_hat-yi)
            # compute gradient
            d_li = 2*xi*(y_hat-yi)
            gradients = gradients + d_li
            sum_loss = sum_loss + li
        sum_loss = sum_loss/batch_size
        losses.append(sum_loss)
        # update weight
        theta = theta - lr*gradients

print("theta = \n", theta)
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




