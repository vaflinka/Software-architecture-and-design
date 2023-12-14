from graphviz import Digraph

# Створюємо об'єкт Digraph
dot = Digraph(comment='Class Diagram')

# Додаємо клас Студент
dot.node('Student', '{Студент| -id: int\n -ім\'я: str\n -курс: int\n +зарахуватись()}\n')

# Додаємо клас Викладач
dot.node('Teacher', '{Викладач| -id: int\n -ім\'я: str\n -предмети: List[Subject]\n +вести_заняття()}\n')

# Додаємо клас Дисципліна
dot.node('Subject', '{Дисципліна| -id: int\n -назва: str\n +створити_дисципліну()}\n')

# Додаємо клас Проходження дисциплін
dot.node('Enrollment', '{Проходження дисциплін| -студент: Student\n -дисципліна: Subject\n -оцінка: int\n +завершити_курс()}\n')

# Додаємо асоціації між класами
dot.edge('Student', 'Enrollment', label='1..*')
dot.edge('Subject', 'Enrollment', label='1..*')
dot.edge('Enrollment', 'Teacher', label='1')

# Зберігаємо графік у файл
dot.render('class_diagram', format='png', cleanup=True)

print("Class Diagram створено та збережено в class_diagram.png")
