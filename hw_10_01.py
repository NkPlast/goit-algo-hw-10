import pulp

# Створення моделі
model = pulp.LpProblem("Максимізація виробництва напоїв", pulp.LpMaximize)

# Змінні
L = pulp.LpVariable('Лимонад', lowBound=0, cat='Integer')
F = pulp.LpVariable('Фруктовий_сік', lowBound=0, cat='Integer')

# Функція цілі
model += L + F, "Загальна кількість продукції"

# Обмеження за інгредієнтами
model += 2 * L + 1 * F <= 100, "Обмеження води"
model += 1 * L <= 50, "Обмеження цукру"
model += 1 * L <= 30, "Обмеження лимонного соку"
model += 2 * F <= 40, "Обмеження фруктового пюре"

# Розв'язання задачі
model.solve()

# Виведення результатів
print("Кількість виробленого лимонаду:", pulp.value(L))
print("Кількість виробленого фруктового соку:", pulp.value(F))
print("Максимальна загальна кількість продукції:", pulp.value(model.objective))
