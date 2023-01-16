from flask import Flask, jsonify, request 
from flask_cors import CORS 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Todos 

app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
CORS(app)
Migrate(app, db)

@app.route("/", methods=["GET"])
def home():
    todos = Todos.query.all()
    todos_serializados = list(map(lambda todos: todos.serialize(), todos))
    return jsonify(todos_serializados)

@app.route("/create_todo", methods=["POST"])
def create_todo():
    todo = Todos()
    todo.title = request.json.get("title")
    todo.body =  request.json.get("body")
    todo.done = request.json.get("done")
    
    db.session.add(todo)
    db.session.commit()

    return "todo creada"

@app.route("/update/<int:id>", methods=["PUT"])
def update(id):
    todo = Todos.query.get(id)
    todo.title = request.json.get("title")
    todo.body =  request.json.get("body")
    todo.done = request.json.get("done")

    db.session.add(todo)
    db.session.commit()

    return "todo editada"

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todos.query.get(id)

    db.session.delete(todo)
    db.session.commit()

    return "todo eliminada"


app.run(host="localhost", port=8080)