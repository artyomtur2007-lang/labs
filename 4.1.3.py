import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Polygon

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

y_offset = -2

body = Ellipse((0, 0 + y_offset), 12, 16, facecolor='#8B4513', edgecolor='black', linewidth=2)
ax.add_patch(body)

head = Circle((0, 5 + y_offset), 5.5, facecolor='#8B4513', edgecolor='black', linewidth=2)
ax.add_patch(head)

left_eye = Circle((-2, 6 + y_offset), 2.2, facecolor='white', edgecolor='black', linewidth=2)
right_eye = Circle((2, 6 + y_offset), 2.2, facecolor='white', edgecolor='black', linewidth=2)
ax.add_patch(left_eye)
ax.add_patch(right_eye)

left_pupil = Circle((-2, 6 + y_offset), 0.9, facecolor='black')
right_pupil = Circle((2, 6 + y_offset), 0.9, facecolor='black')
ax.add_patch(left_pupil)
ax.add_patch(right_pupil)

beak = Polygon([(0, 3 + y_offset), (-1, 2 + y_offset), (1, 2 + y_offset)], facecolor='orange', edgecolor='black')
ax.add_patch(beak)

left_wing = Ellipse((-4, -2 + y_offset), 6, 10, angle=30, facecolor='#654321', edgecolor='black', linewidth=2)
right_wing = Ellipse((4, -2 + y_offset), 6, 10, angle=-30, facecolor='#654321', edgecolor='black', linewidth=2)
ax.add_patch(left_wing)
ax.add_patch(right_wing)

left_foot = Polygon([(-2, -7 + y_offset), (-3, -9 + y_offset), (-1, -9 + y_offset)], facecolor='orange')
right_foot = Polygon([(2, -7 + y_offset), (1, -9 + y_offset), (3, -9 + y_offset)], facecolor='orange')
ax.add_patch(left_foot)
ax.add_patch(right_foot)

left_ear = Polygon([(-3, 10 + y_offset), (-4.5, 12.5), (-1.5, 10.5)], facecolor='#8B4513', edgecolor='black')
right_ear = Polygon([(3, 10 + y_offset), (4.5, 12.5), (1.5, 10.5)], facecolor='#8B4513', edgecolor='black')
ax.add_patch(left_ear)
ax.add_patch(right_ear)

plt.title('Сова', fontsize=14, pad=20)
plt.tight_layout()
plt.show()