import matplotlib.pyplot as plt

# Створюємо граф
plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], marker='o')

# Позначаємо точки
events = ['Запит на бронювання', 'Створення бронювання', 'Отримання підтвердження бронювання',
          'Запит на заселення', 'Заселення', 'Отримання підтвердження заселення',
          'Запит на виселення', 'Виселення']

for i, txt in enumerate(events):
    plt.annotate(txt, (i + 1, i + 1), textcoords="offset points", xytext=(0, 5), ha='center')

# Налаштовуємо графік
plt.title('Activity Diagram: Взаємодія менеджера з базою даних')
plt.xlabel('Кроки')
plt.ylabel('Кроки')

# Виводимо графік
plt.show()
