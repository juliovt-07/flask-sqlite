import sqlite3
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route('/tarefas', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM tasks")
    tasks = [
        {"id": task[0], "title": task[1], "description": task[2]}
        for task in cursor.fetchall()
    ]
    conn.close()
    return jsonify(tasks)

@app.route('/tarefas', methods=['POST'])
def add_task():
    task_data = request.get_json()

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (id, title, description) VALUES (?, ?, ?)",
        (str(uuid.uuid4()), task_data["title"], task_data["description"])
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully"}), 201

@app.route('/tarefas/<task_id>', methods=['PUT'])
def update_task(task_id):
    task_data = request.get_json()

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ? WHERE id = ?",
        (task_data["title"], task_data["description"], task_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Task updated successfully"})

@app.route('/tarefas/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run()
