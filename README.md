## Обчислення визначеного інтеграла методом Монте-Карло

У цьому завданні ми обчислили значення інтеграла функції \( f(x) = x^2 \) на інтервалі [0, 2] методом Монте-Карло та порівняли його з точним значенням, отриманим за допомогою функції `quad` з бібліотеки SciPy.

### Результати обчислень:

- **Інтеграл методом Монте-Карло**: приблизно 2.666 (значення залежить від вибірки)
- **Інтеграл з функцією `quad`**: 2.666666666666667
- **Аналітичний інтеграл**: 2.6666666666666665

### Висновки

Метод Монте-Карло є ефективним чисельним методом для обчислення визначених інтегралів. Він забезпечує достатню точність при великій кількості вибірок. Наші результати підтверджують правильність розрахунків методом Монте-Карло в порівнянні з точним значенням, отриманим аналітично.

- **Відхилення методу Монте-Карло від аналітичного результату**: дуже мале, що свідчить про високу точність цього методу.
- **Відхилення функції `quad` від аналітичного результату**: також дуже мале і знаходиться в межах допустимої похибки.
