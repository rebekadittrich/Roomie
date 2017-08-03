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
    coordx = db.Column(db.Integer)
    coordy = db.Column(db.Integer)
    floor = db.Column(db.Integer)

    def __init__(self, name, area, nearestcheckpoint, coordx, coordy, floor):
        self.name = name
        self.area = area
        self.nearestcheckpoint = nearestcheckpoint
        self.coordx = coordx
        self.coordy = coordy
        self.floor = floor

    def __repr__(self):
        return '{name}'.format(
            name=self.name
        )
    def to_dict(self):
        return {
            "name": self.name,
            "area": self.area,
            "nearestcheckpoint": self.nearestcheckpoint,
            "coordx": self.coordx,
            "coordy": self.coordy,
            "floor": self.floor,
        }
class Checkpoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pointx = db.Column(db.Integer)
    pointy = db.Column(db.Integer)
    floor = db.Column(db.Integer)

    def __init__(self, pointx, pointy, floor):
        self.pointx = pointx
        self.pointy = pointy
        self.floor = floor

    def __repr__(self):
        return '{pointx} {pointy}'.format(
            pointx=self.pointx,
            pointy=self.pointy
        )

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

samecheckpoint = 0

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    nodes = graph[start]
    shortest = None
    for node in nodes:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest


@app.route("/direction/")
def route():
    searchFrom = request.args.get('searchFrom')
    searchTo = request.args.get('searchTo')
    if searchFrom == "Cat%27s%20cradle":
        searchFrom = "Cat\'s cradle"
    if searchTo == "Cat%27s%20cradle":
        searchTo = "Cat\'s cradle"
    from_room = Room.query.filter_by(name=searchFrom)[0]
    to_room = Room.query.filter_by(name=searchTo)[0]

    coords = [from_room.coordx, from_room.coordy, to_room.coordx, to_room.coordy]


    graph = defaultdict(list)
    for line in Line.query.all():
        graph[line.fromid].append(line.toid)
    sol = find_shortest_path(graph, from_room.nearestcheckpoint, to_room.nearestcheckpoint)
    path = []

    checkcoordsall = []
    checkcoordsall0 = []
    checkcoordsall1 = []
    checkcoordsall2 = []
    checkcoordsall3 = []

    print sol

    checkcoordsall.append(from_room.coordx)
    checkcoordsall.append(from_room.coordy)

    for i in range(0, len(sol) - 1):
        steps = Line.query.filter_by(fromid=sol[i], toid=sol[i+1]).first()
        path.append(str(steps.desc))

    for i in range(0, len(sol)):
        checkcoords = Checkpoint.query.filter_by(id=sol[i]).first()
        checkcoordsall.append(checkcoords.pointx)
        checkcoordsall.append(checkcoords.pointy)
        if checkcoords.floor == 0:
            checkcoordsall0.append(checkcoords.pointx)
            checkcoordsall0.append(checkcoords.pointy)
        elif checkcoords.floor == 1:
            checkcoordsall1.append(checkcoords.pointx)
            checkcoordsall1.append(checkcoords.pointy)
        elif checkcoords.floor == 2:
            checkcoordsall2.append(checkcoords.pointx)
            checkcoordsall2.append(checkcoords.pointy)
        else:
            checkcoordsall3.append(checkcoords.pointx)
            checkcoordsall3.append(checkcoords.pointy)

    checkcoordsall.append(to_room.coordx)
    checkcoordsall.append(to_room.coordy)
    if from_room.nearestcheckpoint == to_room.nearestcheckpoint:
        path = ["You are almost there"]

    return json.dumps({
        "path": path,
        "coords": coords,
        "checkcoordsall": checkcoordsall,
        "checkcoordsall0": checkcoordsall0,
        "checkcoordsall1": checkcoordsall1,
        "checkcoordsall2": checkcoordsall2,
        "checkcoordsall3": checkcoordsall3,
    })

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

