import matplotlib.pyplot as plt
import math

x = []
x_rad = []
f_x = []
h_x = []

for i in range(500):
    xi = -360 + i * (720 / 499)
    x.append(xi)

    xi_rad = xi * 3.14159 / 180
    x_rad.append(xi_rad)

    part1 = math.exp(math.cos(xi_rad))
    part2 = math.log(math.cos(0.6 * xi_rad) ** 2 + 1) * math.sin(xi_rad)
    f_x.append(part1 + part2)

    part3 = math.log((math.cos(xi_rad) + math.sin(xi_rad)) ** 2 + 2.5) + 10
    h_x.append(-part3)

plt.plot(x_rad, f_x, 'b-')
plt.plot(x_rad, h_x, 'g-')
plt.xlabel("Градусы")
plt.ylabel("Y")
plt.title("Grafics 1")
plt.show()