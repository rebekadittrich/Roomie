import os
from collections import defaultdict
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
    nearestcheckpoint = db.Column(db.Integer)

    def __init__(self, name, area, nearestcheckpoint):
        self.name = name
        self.area = area
        self.nearestcheckpoint = nearestcheckpoint

    def __repr__(self):
        return 'Room {name}'.format(
            name=self.name
        )
    def to_dict(self):
        return {
            "name": self.name,
            "area": self.area,
            "nearestcheckpoint": self.nearestcheckpoint,
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

class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fromid = db.Column(db.Integer)
    toid = db.Column(db.Integer)
    distance = db.Column(db.Integer)
    desc = db.Column(db.String(3000))

    def __init__(self, fromid, toid, distance, desc):
        self.fromid = fromid
        self.toid = toid
        self.distance = distance
        self.desc = desc

    def __repr__(self):
        return '{fromid} {toid}'.format(
            fromid=self.fromid,
            toid=self.toid
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


def find_shortest_path(graph, start, end, path=[], totaldistance=0):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return 'You are almost there'
    nodes = graph[start]
    shortest = None
    for node in nodes:
        if node not in path:
            totaldistance += 1
            newpath = find_shortest_path(graph, node, end, path, totaldistance)
            if newpath:
                if not shortest or totaldistance < shortestdistance:
                    shortest = newpath
                    shortestdistance = totaldistance
    return shortest


@app.route("/direction/")
def route():
    searchFrom = request.args.get('searchFrom')
    searchTo = request.args.get('searchTo')
    if searchFrom == "Cat%27s%20cradle":
        searchFrom = "Cat\'s cradle"
    if searchTo == "Cat\'s cradle":
        searchTo = "Cat\'s cradle"
    from_room = Room.query.filter_by(name=searchFrom)[0]
    to_room = Room.query.filter_by(name=searchTo)[0]

    graph = defaultdict(list)
    for line in Line.query.all():
        graph[line.fromid].append(line.toid)

    sol = find_shortest_path(graph, from_room.nearestcheckpoint, to_room.nearestcheckpoint)
    path = []
    for i in range(0, len(sol) - 1):
        alma = Line.query.filter_by(fromid=sol[i], toid=sol[i+1]).first()
        path.append(alma.desc)
    return json.dumps(path)


shortestdistance = 100000000


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

