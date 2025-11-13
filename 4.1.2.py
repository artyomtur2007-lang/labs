import matplotlib.pyplot as plt

x = []
y = []

for i in range(1000):
    xi = -10 + i * 0.02
    x.append(xi)
    if xi != 3 and xi != -3:
        y.append(5 / (xi**2 - 9))
    else:
        y.append(0)

plt.plot(x, y, 'r-', linewidth=2)
plt.xlabel('x')
plt.ylabel('f_x')
plt.title("Grafic 2")
plt.ylim(-10, 10)
plt.show()