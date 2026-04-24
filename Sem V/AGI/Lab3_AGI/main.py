import numpy as np
import matplotlib.pyplot as plt

# Punctele de control inițiale pentru curbă Bezier
b0 = np.array([-3, 1])
b1 = np.array([-4, 4])
b2 = np.array([4, 4])
b3 = np.array([3, 1])
puncte_de_control = np.array([b0, b1, b2, b3])

# Funcție pentru calculul unei curbe Bezier
def bezier_curve(points, t_values):
    n = len(points) - 1
    curve_points = []
    for t in t_values:
        temp_points = points.copy()
        for r in range(1, n + 1):
            temp_points[:n - r + 1] = (1 - t) * temp_points[:n - r + 1] + t * temp_points[1:n - r + 2]
        curve_points.append(temp_points[0])
    return np.array(curve_points)

# Exercițiul 1: Ridicarea gradului
def elevate_degree(points):
    n = len(points) - 1
    elevated_points = [points[0]]  # Primul punct rămâne același
    for i in range(1, n + 1):
        elevated_point = (i / (n + 1)) * points[i - 1] + (1 - i / (n + 1)) * points[i]
        elevated_points.append(elevated_point)
    elevated_points.append(points[-1])  # Ultimul punct rămâne același
    return np.array(elevated_points)

# Exercițiul 2: Divizarea curbei la t = 1/3
def de_casteljau_subdivision(points, t):
    n = len(points) - 1
    left_points = [points[0]]
    right_points = [points[-1]]
    temp_points = points.copy()
    for r in range(1, n + 1):
        temp_points[:n - r + 1] = (1 - t) * temp_points[:n - r + 1] + t * temp_points[1:n - r + 2]
        left_points.append(temp_points[0])
        right_points.append(temp_points[n - r])
    return np.array(left_points), np.array(right_points[::-1])  # Reverse right_points

# Generăm valori de t pentru a trasa curbele
t_values = np.linspace(0, 1, 100)

# Curba originală și poligonul de control pentru gradul 3
curve_3 = bezier_curve(puncte_de_control, t_values)

# Ridicăm gradul la 4 și generăm curba nouă
elevated_control_points = elevate_degree(puncte_de_control)
curve_4 = bezier_curve(elevated_control_points, t_values)

# Divizăm curbă la t = 1/3
t_divide = 1/3
left_points, right_points = de_casteljau_subdivision(puncte_de_control, t_divide)
curve_left = bezier_curve(left_points, t_values)
curve_right = bezier_curve(right_points, t_values)

# Reprezentare grafică
plt.figure(figsize=(12, 6))

# Graficul Exercițiul 1
plt.subplot(1, 2, 1)
plt.plot(curve_3[:, 0], curve_3[:, 1], label='Curba Bézier de gradul 3', color='blue')
plt.plot(curve_4[:, 0], curve_4[:, 1], label='Curba Bézier de gradul 4', color='orange')
plt.plot(puncte_de_control[:, 0], puncte_de_control[:, 1], 'bo-', label='Puncte de control gradul 3')
plt.plot(elevated_control_points[:, 0], elevated_control_points[:, 1], 'ro-', label='Puncte de control gradul 4')
plt.title("Ridicarea gradului curbei Bézier")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

# Graficul Exercițiul 2
plt.subplot(1, 2, 2)
plt.plot(curve_left[:, 0], curve_left[:, 1], label='Segment stânga (t=1/3)', color='green')
plt.plot(curve_right[:, 0], curve_right[:, 1], label='Segment dreapta (t=1/3)', color='purple')
plt.plot(puncte_de_control[:, 0], puncte_de_control[:, 1], 'bo-', label='Puncte de control originale')
plt.plot(left_points[:, 0], left_points[:, 1], 'go--', label='Puncte control segment stânga')
plt.plot(right_points[:, 0], right_points[:, 1], 'mo--', label='Puncte control segment dreapta')
plt.title("Divizarea curbei Bézier la t=1/3")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
