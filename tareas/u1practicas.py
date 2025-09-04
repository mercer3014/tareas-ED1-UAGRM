# ==============================
# 1. STATIC REPRESENTATION
# ==============================

catalog = {}  # Diccionario estático para almacenar libros

def add_book(title, author, isbn, genre):
    """Agrega un libro al catálogo"""
    catalog[isbn] = {'title': title, 'author': author, 'genre': genre}

def search_book(query):
    """Busca libros por título, autor o ISBN"""
    results = []
    for isbn, book_data in catalog.items():
        if query in book_data['title'] or query in book_data['author'] or query == isbn:
            results.append(book_data)
    return results

def display_catalog():
    """Muestra todos los libros del catálogo"""
    for isbn, book_data in catalog.items():
        print(f"ISBN: {isbn}, Title: {book_data['title']}, Author: {book_data['author']}, Genre: {book_data['genre']}")

# Ejemplo de uso
print("\n=== Static Representation ===")
add_book("The Lord of the Rings", "J.R.R. Tolkien", "9780547928227", "Fantasy")
add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "9780345391803", "Science Fiction")

print("Search Results:", search_book("Tolkien"))
display_catalog()


# ==============================
# 2. DYNAMIC REPRESENTATION
# ==============================

transactions = []  # Lista dinámica para transacciones

def deposit(amount):
    """Registra un depósito"""
    transactions.append({'type': 'deposit', 'amount': amount})

def withdraw(amount):
    """Registra un retiro"""
    transactions.append({'type': 'withdrawal', 'amount': amount})

def view_history():
    """Muestra el historial de transacciones"""
    print("\nTransaction History:")
    for transaction in transactions:
        print(f"{transaction['type'].capitalize()}: {transaction['amount']}")

def check_balance():
    """Calcula el saldo actual"""
    balance = 0
    for transaction in transactions:
        if transaction['type'] == 'deposit':
            balance += transaction['amount']
        else:
            balance -= transaction['amount']
    return balance

# Ejemplo de uso
print("\n=== Dynamic Representation ===")
deposit(1000)
withdraw(200)
deposit(500)
view_history()
print(f"Current balance: {check_balance()}")


# ==============================
# 3. PERSISTENT REPRESENTATION
# ==============================

def load_todo_list(filename="todo.txt"):
    """Carga la lista de tareas desde un archivo"""
    tasks = []
    try:
        with open(filename, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # Si no existe el archivo, no pasa nada
    return tasks

def save_todo_list(tasks, filename="todo.txt"):
    """Guarda la lista de tareas en un archivo"""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks, task):
    """Agrega una nueva tarea"""
    tasks.append(task)

def mark_complete(tasks, task_index):
    """Marca una tarea como completa"""
    if 0 <= task_index < len(tasks):
        tasks[task_index] = tasks[task_index] + " [Complete]"

def view_todo_list(tasks):
    """Muestra la lista de tareas"""
    print("\nTo-Do List:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

# Ejemplo de uso
print("\n=== Persistent Representation ===")
todo_list = load_todo_list()
add_task(todo_list, "Buy groceries")
add_task(todo_list, "Finish homework")
view_todo_list(todo_list)
mark_complete(todo_list, 0)
view_todo_list(todo_list)
save_todo_list(todo_list)


# ==============================
# 4. SIMULATED REPRESENTATION
# ==============================

import random
import time

class Car:
    def __init__(self, direction):
        self.direction = direction
        self.position = 0

class TrafficLight:
    def __init__(self):
        self.color = "red"

    def change_color(self):
        """Alterna entre rojo y verde"""
        self.color = "green" if self.color == "red" else "red"

# Ejemplo de simulación
print("\n=== Simulated Representation ===")
cars = [Car(random.choice(["North", "South", "East", "West"])) for _ in range(3)]
traffic_light = TrafficLight()

for step in range(3):
    print(f"\nStep {step + 1}")
    traffic_light.change_color()
    print(f"Traffic light is {traffic_light.color}")
    for car in cars:
        if traffic_light.color == "green":
            car.position += 1
        print(f"Car from {car.direction} is at position {car.position}")
    time.sleep(1)
