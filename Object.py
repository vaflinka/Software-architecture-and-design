from graphviz import Digraph

def create_evolution_diagram():
    # Створюємо граф Object діаграми
    graph = Digraph('G', filename='evolution_diagram', format='png', engine='dot')

    # Додаємо об'єкти: різні види та їх еволюційний розвиток
    graph.node('Вид_1')
    graph.node('Вид_2')
    graph.node('Вид_3')
    graph.node('Еволюційний_розвиток')

    # Додаємо зв'язки між об'єктами
    graph.edge('Вид_1', 'Еволюційний_розвиток')
    graph.edge('Вид_2', 'Еволюційний_розвиток')
    graph.edge('Вид_3', 'Еволюційний_розвиток')

    # Зберігаємо граф у файл
    graph.render(view=True)

if __name__ == "__main__":
    create_evolution_diagram()
