import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return np.sin(x)

# Межі інтегрування
a = 0
b = np.pi

# Метод Монте-Карло для обчислення інтеграла
def monte_carlo_integrate(f, a, b, num_samples):
    samples = np.random.uniform(a, b, num_samples)
    sample_values = f(samples)
    integral = (b - a) * np.mean(sample_values)
    return integral

# Кількість зразків для методу Монте-Карло
num_samples = 10_000
mc_integral = monte_carlo_integrate(f, a, b, num_samples)

# Аналітичне обчислення інтеграла за допомогою SciPy
quad_integral, error = spi.quad(f, a, b)

# Виведення результатів
print(f"Інтеграл методом Монте-Карло: {mc_integral}")
print(f"Інтеграл методом quad: {quad_integral}")
print(f"Абсолютна помилка методу Монте-Карло: {abs(mc_integral - quad_integral)}")

# Побудова графіка
x = np.linspace(-0.5, np.pi + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
