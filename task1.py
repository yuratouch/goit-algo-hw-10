import pulp

# Створення проблеми максимізації
prob = pulp.LpProblem("Maximize Drink Production", pulp.LpMaximize)

# Змінні, які визначають кількість "Лимонаду" та "Фруктового соку"
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Continuous')

# Функція цілі: максимізація загальної кількості вироблених продуктів
prob += lemonade + fruit_juice, "Total Production"

# Обмеження на ресурси
prob += 2 * lemonade + fruit_juice <= 100, "Water Constraint"
prob += 1 * lemonade <= 50, "Sugar Constraint"
prob += 1 * lemonade <= 30, "Lemon Juice Constraint"
prob += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язання проблеми
prob.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Optimal number of Lemonade: {pulp.value(lemonade)}")
print(f"Optimal number of Fruit Juice: {pulp.value(fruit_juice)}")
print(f"Total Production: {pulp.value(prob.objective)}")
