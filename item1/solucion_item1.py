# Solución ítem 1
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

x = np.linspace(-0.5, 6.5, 400)
y = f(x)

puntos = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]
colores = ['red', 'green', 'blue', 'magenta', 'cyan']
labels = [
    'Tangente en x=0',
    'Tangente en x=π/4',
    'Tangente en x=π/2',
    'Tangente en x=π',
    'Tangente en x=3π/2'
]

plt.figure(figsize=(12, 6))
plt.plot(x, y, color='black', linewidth=2, label='f(x) = sin(x)')

delta = 1
for x0, color, label in zip(puntos, colores, labels):
    y0 = f(x0)
    pendiente = df(x0)
    x_tan = np.linspace(x0 - delta, x0 + delta, 50)
    y_tan = y0 + pendiente * (x_tan - x0)
    plt.plot(x_tan, y_tan, color=color, linewidth=2, label=label)
    plt.scatter(x0, y0, color=color, s=60, zorder=5)

plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.grid(alpha=0.3)
plt.title('Rectas tangentes a f(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.xlim(-0.5, 6.5)
plt.ylim(-1.1, 1.5)
plt.show()
