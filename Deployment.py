from graphviz import Digraph

# Створюємо граф Deployment діаграми
graph = Digraph('Deployment', filename='deployment_diagram', format='png', engine='dot')

# Додаємо компоненти: базу даних, сервер, клієнт
graph.node('Database', shape='box', color='blue')
graph.node('Server', shape='box', color='green')
graph.node('Client', shape='box', color='red')

# Додаємо зв'язки між компонентами
graph.edge('Database', 'Server', label='Connection')
graph.edge('Server', 'Client', label='Communication')

# Зберігаємо граф у файл
graph.render(view=True)
