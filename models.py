from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todos(db.Model):
    tablename = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(500))
    done = db.Column(db.Boolean, default=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "body":self.body,
            "done": self.done,
        }