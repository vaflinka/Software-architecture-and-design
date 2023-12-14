from graphviz import Digraph

# Створюємо об'єкт Digraph
dot = Digraph(comment='Use Case Diagram')

# Додаємо користувача та бібліотекаря
dot.node('User', 'Користувач')
dot.node('Librarian', 'Бібліотекар')

# Додаємо use cases
dot.node('AddBook', 'Додати нову книжку в бібліотеку')
dot.node('CheckAvailability', 'Запит про наявність книжки')
dot.node('RegisterReceipt', 'Реєстрація отримання книжки')
dot.node('RegisterReturn', 'Реєстрація повернення книжки')

# Додаємо відносини
dot.edge('User', 'AddBook')
dot.edge('User', 'CheckAvailability')
dot.edge('User', 'RegisterReceipt')
dot.edge('User', 'RegisterReturn')

dot.edge('Librarian', 'AddBook')
dot.edge('Librarian', 'CheckAvailability')
dot.edge('Librarian', 'RegisterReceipt')
dot.edge('Librarian', 'RegisterReturn')

# Зберігаємо графік у файл
dot.render('use_case_diagram', format='png', cleanup=True)

print("Use Case Diagram створено та збережено в use_case_diagram.png")
