from roomie import db
db.create_all()

from roomie import Room

db.session.add(Room('spline', 'Talent/DLR/Community', 4))
db.session.add(Room('cat\'s cradle', 'Talent/DLR/Community', 6))
db.session.add(Room('hypercube', 'Talent/DLR/Community', 3))
db.session.add(Room('fractal', 'Talent/DLR/Community', 3))
db.session.add(Room('icosidodecahedron', 'Talent/DLR/Community', 10))
db.session.add(Room('Eames', 'Design/UX/Finance', 4))
db.session.add(Room('Regina', 'Design/UX/Finance', 6))
db.session.add(Room('Lovelace', 'Design/UX/Finance', 2))
db.session.add(Room('Turing', 'Design/UX/Finance', 8))
db.session.add(Room('Bob', 'Design/UX/Finance', 5))
db.session.add(Room('Erdos', 'Design/UX/Finance', 4))
db.session.add(Room('ContentArranger', 'Support/Marketing', 6))
db.session.add(Room('EagleTransition', 'Support/Marketing', 4))
db.session.add(Room('UserCell', 'Support/Marketing', 4))
db.session.add(Room('AbstractElement', 'Support/Marketing', 5))
db.session.add(Room('please', 'Support/Marketing', 6))
db.session.add(Room('workshop', 'House of ideas', 30))
db.session.add(Room('geographer', 'Little Prince', 7))
db.session.add(Room('asteroid b-612', 'Little Prince', 7))
db.session.add(Room('elephant', 'Little Prince', 10))
db.session.add(Room('lamplighter', 'Little Prince', 4))
db.session.add(Room('rose', 'FOX', 10))
db.session.add(Room('baobab', 'FOX', 10))
db.session.add(Room('cinema', 'FOX', 8))
db.session.add(Room('Totoro', 'Bento', 4))
db.session.add(Room('Sangaku', 'Bento', 6))
db.session.add(Room('Donkey Kong', 'Bento', 4))
db.session.add(Room('Fuji', 'Bento', 7))
db.session.add(Room('Stretch', 'Values', 12))

db.session.commit()

Room.query.all()


