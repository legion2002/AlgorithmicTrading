import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(100)

inps = [(25, 5), (12, 7), (15, 7), (14, 9), (19, 12), (23, 9), (25, 9), (29, 4), (21, 12)]
labels = [1, 0, 0, 0, 0, 1, 1, 1, 0]

fig = plt.figure()

df_dict = {'x': [],
           'y': [],
           'z': labels[:]}

for inp in inps:
  df_dict['x'].append(inp[0])
  df_dict['y'].append(inp[1])

df = pd.DataFrame(df_dict)

groups = df.groupby('z')
for name, group in groups:
    plt.plot(group.x, group.y, marker='o', linestyle='', markersize=12, label=name)

plt.legend()
plt.xlim(0, 30)
plt.ylim(0, 30)
plt.show()

learning_rate = 0.001

weights = np.random.randn(2,1)
weights_grad = np.zeros_like(weights)
bias = np.random.randn()
bias_grad = 0
print(weights, bias, weights_grad, bias_grad)

def forward(x):
  global weights
  global bias
  x = np.array(list(x)).reshape(2,1)
  return (1 if weights.T@x + bias>=0 else 0), weights.T@x + bias

def calc_loss(x, y):
  prediction, _ = forward(x)
  return 0.5*(y - prediction)**2

def backpropagate(x, y, prediction):
  global weights_grad
  global bias_grad
  u = np.array(list(x)).reshape(2,1)
  weights_grad -= (y - prediction)*u
  bias_grad -= (y - prediction)

def gradient_descent():
  global weights_grad
  global bias_grad
  global weights
  global bias
  global learning_rate
  weights -= learning_rate*weights_grad
  bias -= learning_rate*bias_grad

def zero_grads():
  global weights_grad
  global bias_grad
  global weights
  weights_grad = np.zeros_like(weights)
  bias_grad = 0

def plot_line(epoch):
  global groups
  from functools import partial

  import numpy
  import scipy.optimize
  import matplotlib.pyplot as plt

  def z(x, y):
    _, val = forward((x,y))
    return np.squeeze(val)

  xs = []
  ys = []
  for x in numpy.linspace(0, 30, num=200):
    try:
        y = scipy.optimize.brentq(partial(z, x), 0, 30)
    except ValueError:
        pass
    else:
        xs.append(x)
        ys.append(y)

  plt.plot(xs, ys)
  for name, group in groups:
      plt.plot(group.x, group.y, marker='o', linestyle='', markersize=12, label=name)

  plt.legend()
  plt.xlim(0, 30)
  plt.ylim(0, 30)
  plt.title("Epoch: {}".format(epoch))
  fig.canvas.draw()

weights = np.random.randn(2,1)
weights_grad = np.zeros_like(weights)
bias = np.random.randn()
bias_grad = 0
weights, bias, weights_grad, bias_grad

epochs = 100

for epoch in range(epochs):
  plt.cla()
  for inp,lab in zip(inps,labels):
    forw, val = forward(inp)
    backpropagate(inp, lab, forw)
  gradient_descent()
  zero_grads()
  epoch+=1
  plot_line(epoch)
  plt.pause(0.1)