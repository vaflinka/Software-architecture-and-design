from graphviz import Digraph

def create_email_verification_sequence_diagram():
    # Створюємо граф Sequence діаграми
    graph = Digraph('G', filename='email_verification_sequence_diagram', format='png', engine='dot')

    # Додаємо об'єкти: Комп'ютер та Сервер
    graph.node('Комп\'ютер', shape='box', color='blue')
    graph.node('Сервер', shape='box', color='green')

    # Додаємо повідомлення та зв'язки між об'єктами
    graph.edge('Комп\'ютер', 'Сервер', label='надіслати Email')
    graph.edge('Сервер', 'Комп\'ютер', label='відповідь')
    graph.edge('Комп\'ютер', 'Сервер', label='новий Email')
    graph.edge('Сервер', 'Комп\'ютер', label='вивантажити Email')
    graph.edge('Комп\'ютер', 'Сервер', label='видалити старі Email')

    # Зберігаємо граф у файл
    graph.render(view=True)

if __name__ == "__main__":
    create_email_verification_sequence_diagram()
