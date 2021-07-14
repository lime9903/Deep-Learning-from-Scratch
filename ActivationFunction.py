import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    y = x > 0    # Bool로 출력
    return y.astype(np.int64)   # y의 자료형을 int로 바꾸기

def sigmoid(x):
    return 1 / (1+np.exp(-x))   

x = np.arange(-5, 5, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # y축 범위 지정

x1 = np.arange(-5, 5, 0.1)
y1 = sigmoid(x1)
plt.plot(x1, y1, linestyle='--')
plt.ylim(-0.1, 1.1)
plt.show() 