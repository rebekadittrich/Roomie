import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{cwd}/test.db'.format(cwd=os.getcwd())
db = SQLAlchemy(app)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    area = db.Column(db.String(120))
    capacity = db.Column(db.Integer)
    occupied = db.Column(db.Boolean)

    def __init__(self, name, area, capacity):
        self.name = name
        self.area = area
        self.capacity = capacity
        self.occupied = False

    def __repr__(self):
        return 'Room {name}'.format(
            name=self.name
        )


@app.route("/")
def index():
    rows = Room.query.all()
    return render_template('Template.html', rows=rows)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)

