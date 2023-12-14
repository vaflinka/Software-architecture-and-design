from graphviz import Digraph

def create_communication_diagram():
    # Створюємо граф Communication діаграми
    graph = Digraph('G', filename='communication_diagram', format='png', engine='dot')

    # Додаємо вузли: клієнт та колл-центр
    graph.node('Клієнт', shape='box', color='blue')
    graph.node('Колл-центр', shape='box', color='green')

    # Додаємо зв'язки між вузлами
    graph.edge('Клієнт', 'Колл-центр', label='Запит на консультацію')
    graph.edge('Колл-центр', 'Клієнт', label='Відповідь та консультація')
    graph.edge('Клієнт', 'Колл-центр', label='Подяка за допомогу')

    # Зберігаємо граф у файл
    graph.render(view=True)

if __name__ == "__main__":
    create_communication_diagram()
