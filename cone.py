import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definindo as funções
def f_pos(x, y):
    return np.sqrt(x**2 + y**2)  # Cone superior

def f_neg(x, y):
    return -np.sqrt(x**2 + y**2)  # Cone inferior

# Criando os dados para x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z_pos = f_pos(X, Y)  # Valores do cone superior
Z_neg = f_neg(X, Y)  # Valores do cone inferior

# Criando o gráfico 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotando os dois cones
surf_pos = ax.plot_surface(X, Y, Z_pos, cmap='viridis', alpha=0.7, label='$f(x,y) = \sqrt{x^2 + y^2}$')
surf_neg = ax.plot_surface(X, Y, Z_neg, cmap='plasma', alpha=0.7, label='$f(x,y) = -\sqrt{x^2 + y^2}$')

# Adicionando rótulos e título
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Cones: $f(x,y) = \sqrt{x^2 + y^2}$ e $f(x,y) = -\sqrt{x^2 + y^2}$')

# Linha na origem para destacar z=0
ax.plot([0, 0], [0, 0], [-5, 5], color='red', linestyle='--', linewidth=2, label='z = 0')

plt.show()