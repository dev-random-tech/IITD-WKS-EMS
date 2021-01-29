import random
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#plt.style.use("fivethirtyeight")

#x_vals = [0,1,2,3,4,5]
#y_vals = [0,1,3,2,3,5]
x_vals = []
y_vals = []
index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))
    plt.cla()
    plt.plot(x_vals,y_vals)

ani = FuncAnimation(plt.gcf(),animate,interval=1000) #gcf = get current figure
plt.plot(x_vals,y_vals)

plt.tight_layout()
plt.show()
