import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Параметри для методу Монте-Карло
num_samples = 100000

# Створення випадкових точок
x_random = np.random.uniform(a, b, num_samples)
y_random = f(x_random)

# Обчислення середнього значення функції
mean_value = np.mean(y_random)

# Обчислення інтегралу методом Монте-Карло
integral_mc = (b - a) * mean_value

# Обчислення інтегралу за допомогою функції quad
result, error = spi.quad(f, a, b)

# Аналітичний розрахунок інтеграла
integral_analytical = (2**3) / 3

# Порівняння результатів
print(f"Інтеграл методом Монте-Карло: {integral_mc}")
print(f"Інтеграл з функцією quad: {result}")
print(f"Аналітичний інтеграл: {integral_analytical}")
print(f"Відхилення методу Монте-Карло від аналітичного результату: {abs(integral_mc - integral_analytical)}")
print(f"Відхилення функції quad від аналітичного результату: {abs(result - integral_analytical)}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
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
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Створення файлу readme.md з висновками
with open("readme.md", "w") as file:
    file.write("## Обчислення визначеного інтеграла методом Монте-Карло\n")
    file.write("\n")
    file.write("У цьому завданні ми обчислили значення інтеграла функції \( f(x) = x^2 \) на інтервалі [0, 2] методом Монте-Карло та порівняли його з точним значенням, отриманим за допомогою функції `quad` з бібліотеки SciPy.\n")
    file.write("\n")
    file.write("### Результати обчислень:\n")
    file.write("\n")
    file.write(f"- Інтеграл методом Монте-Карло: {integral_mc}\n")
    file.write(f"- Інтеграл з функцією `quad`: {result}\n")
    file.write(f"- Аналітичний інтеграл: {integral_analytical}\n")
    file.write("\n")
    file.write("### Висновки\n")
    file.write("\n")
    file.write("Метод Монте-Карло є ефективним чисельним методом для обчислення визначених інтегралів. Він забезпечує достатню точність при великій кількості вибірок. Наші результати підтверджують правильність розрахунків методом Монте-Карло в порівнянні з точним значенням, отриманим аналітично.\n")
    file.write(f"Відхилення методу Монте-Карло від аналітичного результату: {abs(integral_mc - integral_analytical)}\n")
    file.write(f"Відхилення функції `quad` від аналітичного результату: {abs(result - integral_analytical)}\n")
