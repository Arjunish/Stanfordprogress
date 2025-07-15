import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(-1, 1, 100)
'''line2, = ax.plot(x, 0.8 * np.sin(28 * x + 0.1), color='white')
line, = ax.plot(x, 0.6 * np.sin(42 * x + 0.1), color='white')'''
line3, = ax.plot(x, np.zeros_like(x), color='green')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

def update(frame):
    y1 = 0.8 * np.sin(28 * x + 0.1 * frame)
    y2 = 0.6 * np.sin(42 * x + 0.1 * frame)
    line.set_ydata(y1)
    line2.set_ydata(y2)
    line3.set_ydata(y1 * y2)
    return line, line2, line3

ani = animation.FuncAnimation(fig, update, frames=500, interval=30, blit=True)
plt.show()


