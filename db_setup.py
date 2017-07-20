from roomie import db
db.create_all()

from roomie import Room

db.session.add(Room('Spline', 'Talent/DLR/Community', 4))
db.session.add(Room('Cat\'s cradle', 'Talent/DLR/Community', 6))
db.session.add(Room('Hypercube', 'Talent/DLR/Community', 3))
db.session.add(Room('Fractal', 'Talent/DLR/Community', 3))
db.session.add(Room('Icosidodecahedron', 'Talent/DLR/Community', 10))
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
db.session.add(Room('Please', 'Support/Marketing', 6))
db.session.add(Room('Workshop', 'House of ideas', 30))
db.session.add(Room('Geographer', 'Little Prince', 7))
db.session.add(Room('Asteroid b-612', 'Little Prince', 7))
db.session.add(Room('Elephant', 'Little Prince', 10))
db.session.add(Room('Lamplighter', 'Little Prince', 4))
db.session.add(Room('Rose', 'FOX', 10))
db.session.add(Room('Baobab', 'FOX', 10))
db.session.add(Room('Cinema', 'FOX', 8))
db.session.add(Room('Totoro', 'Bento', 4))
db.session.add(Room('Sangaku', 'Bento', 6))
db.session.add(Room('Donkey Kong', 'Bento', 4))
db.session.add(Room('Fuji', 'Bento', 7))
db.session.add(Room('Stretch', 'Values', 12))

db.session.commit()

Room.query.all()


