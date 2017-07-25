from roomie import db
db.create_all()

from roomie import Room

db.session.add(Room('Spline', 'Talent/DLR/Community', 25))
db.session.add(Room('Cat\'s cradle', 'Talent/DLR/Community', 25))
db.session.add(Room('Hypercube', 'Talent/DLR/Community', 25))
db.session.add(Room('Fractal', 'Talent/DLR/Community', 28))
db.session.add(Room('Icosidodecahedron', 'Talent/DLR/Community', 25))
db.session.add(Room('Eames', 'Design/UX/Finance', 9))
db.session.add(Room('Regina', 'Design/UX/Finance', 9))
db.session.add(Room('Lovelace', 'Design/UX/Finance', 12))
db.session.add(Room('Turing', 'Design/UX/Finance', 10))
db.session.add(Room('Bob', 'Design/UX/Finance', 10))
db.session.add(Room('Erdos', 'Design/UX/Finance', 10))
db.session.add(Room('ContentArranger', 'Support/Marketing', 20))
db.session.add(Room('EagleTransition', 'Support/Marketing', 20))
db.session.add(Room('UserCell', 'Support/Marketing', 18))
db.session.add(Room('AbstractElement', 'Support/Marketing', 18))
db.session.add(Room('Please', 'Support/Marketing', 18))
db.session.add(Room('Workshop', 'House of ideas', 13))
db.session.add(Room('Geographer', 'Little Prince', 7))
db.session.add(Room('Asteroid b-612', 'Little Prince', 7))
db.session.add(Room('Elephant', 'Little Prince', 7))
db.session.add(Room('Lamplighter', 'Little Prince', 7))
db.session.add(Room('Rose', 'FOX', 1))
db.session.add(Room('Baobab', 'FOX', 1))
db.session.add(Room('Cinema', 'FOX', 1))
db.session.add(Room('Totoro', 'Bento', 14))
db.session.add(Room('Sangaku', 'Bento', 17))
db.session.add(Room('Donkey Kong', 'Bento', 14))
db.session.add(Room('Fuji', 'Bento', 16))
db.session.add(Room('Stretch', 'Values', 30))

db.session.commit()

Room.query.all()


