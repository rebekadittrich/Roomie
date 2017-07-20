import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

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
    def to_dict(self):
        return {
            "name": self.name,
            "area": self.area,
            "capacity": self.capacity,
            "occupied": self.occupied
        }

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fromid = db.Column(db.Integer)
    toid = db.Column(db.Integer)
    desc = db.Column(db.String(3000))

    def __init__(self, fromid, toid, desc):
        self.fromid = fromid
        self.toid = toid
        self.desc = desc
    def __repr__(self):
        return 'Route {desc}'.format(
            desc=self.desc
        )



@app.route("/")
def index():
    searchParam = request.args.get('searchParam')
    if searchParam is None:
        rows = Room.query.all()
    else:
        rows = Room.query.filter(
            (Room.name == searchParam) |
            (Room.area == searchParam) |
            (Room.capacity >= searchParam)
        )
    return render_template('Template.html', rows=rows, searchTo=request.args.get('searchTo'))

@app.route("/direction/")
def route():
    searchFrom = request.args.get('searchFrom')
    searchTo = request.args.get('searchTo')

    for room in Room.query.all():
        if searchFrom == room:
            fromname = Room.query.filter_by(name=room).first()
            fromnameid = Route.query.filter_by(fromid=fromname.id)

        if searchTo == room:
            toname = Room.query.filter_by(name=room).first()
            tonameid = Route.query.filter_by(toid=toname.id)

    routeid = Route.query.filter_by(id=list(set(fromnameid).intersection(tonameid)))
    alma = routeid.desc
    return alma

@app.route("/a")
def dict_to_json():
    room_dicts = []
    for room in Room.query.all():
        room_dicts.append(
            room.to_dict()
        )
    return json.dumps(room_dicts)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)

