from graphviz import Digraph

def create_water_state_machine():
    # Створюємо граф State Machine діаграми
    graph = Digraph('G', filename='water_state_machine', format='png', engine='dot')

    # Додаємо стани: лід, вода, пар
    graph.node('Лід')
    graph.node('Вода')
    graph.node('Пар')

    # Додаємо переходи між станами
    graph.edge('Лід', 'Вода', label='Плавлення')
    graph.edge('Вода', 'Пар', label='Випаровування')
    graph.edge('Пар', 'Вода', label='Конденсація')
    graph.edge('Вода', 'Лід', label='Замерзання')

    # Зберігаємо граф у файл
    graph.render(view=True)

if __name__ == "__main__":
    create_water_state_machine()
