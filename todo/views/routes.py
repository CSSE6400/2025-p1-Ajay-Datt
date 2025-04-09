from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__, url_prefix="/api/v1")

todos = {
    1: {
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    }
}

@api.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@api.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(list(todos.values())), 200


@api.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = todos.get(todo_id)
    if todo is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(todo), 200


@api.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    todo_id = max(todos.keys(), default=0) + 1
    todo = {
        "id": todo_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "completed": data.get("completed", False),
        "deadline_at": data.get("deadline_at", None),
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    }
    todos[todo_id] = todo
    return jsonify(todo), 201


@api.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json()
    if todo_id not in todos:
        return jsonify({"error": "Not found"}), 404
    todo = todos[todo_id]
    todo.update({
        "title": data.get("title", todo["title"]),
        "description": data.get("description", todo["description"]),
        "completed": data.get("completed", todo["completed"]),
        "deadline_at": data.get("deadline_at", todo["deadline_at"]),
        "updated_at": "2023-02-20T00:00:00"
    })
    return jsonify(todo), 200


@api.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = todos.pop(todo_id, None)
    if not todo:
        return jsonify({}), 200
    return jsonify(todo), 200
