import sqlite3

def create_table():
    connection = sqlite3.connect('todo.db')
    connection.execute('''CREATE TABLE IF NOT EXISTS TODO_LIST
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TASK TEXT NOT NULL,
        STATUS TEXT NOT NULL,
        DUE_DATE TEXT,
        PRIORITY INTEGER);''')
    connection.commit()
    connection.close()

def add_task(task, due_date=None, priority=None):
    connection = sqlite3.connect('todo.db')
    connection.execute("INSERT INTO TODO_LIST (TASK, STATUS, DUE_DATE, PRIORITY) VALUES(?, 'Incomplete',?,?)", (task,due_date,priority))
    connection.commit()
    print("Task added successfully")
    connection.close()

def list_tasks():
    connection = sqlite3.connect('todo.db')
    cursor = connection.execute("SELECT * FROM TODO_LIST")
    for row in cursor:
        print("Task: ", row[1], " Status: ",row[2], " Due Date: ", row[3], " Priority: ", row[4])
    connection.close()

def update_task(task_id, task=None, due_date=None, priority=None):
    connection = sqlite3.connect('todo.db')
    if task:
        connection.execute("UPDATE TODO_LIST SET TASK = ? WHERE ID = ?", (task, task_id))
    if due_date:
        connection.execute("UPDATE TODO_LIST SET DUE_DATE = ? WHERE ID = ?", (due_date, task_id))
    if priority:
        connection.execute("UPDATE TODO_LIST SET PRIORITY = ? WHERE ID = ?", (priority, task_id))
    connection.commit()
    print("Task updated successfully")
    connection.close()

def mark_complete(task_id):
    connection = sqlite3.connect('todo.db')
    connection.execute("UPDATE TODO_LIST SET STATUS = 'Complete' WHERE ID = ?", (task_id,))
    connection.commit()
    print("Task marked as complete")