from roomie import db
db.create_all()

from roomie import Room

db.session.add(Room('Spline', 'Talent/DLR/Community', 25, 394, 66, 3))
db.session.add(Room('Cat\'s cradle', 'Talent/DLR/Community', 25, 378, 54, 3))
db.session.add(Room('Hypercube', 'Talent/DLR/Community', 25, 363, 46, 3))
db.session.add(Room('Fractal', 'Talent/DLR/Community', 28, 418, 87, 3))
db.session.add(Room('Icosidodecahedron', 'Talent/DLR/Community', 25, 372, 28, 3))
db.session.add(Room('Eames', 'Design/UX/Finance', 9, 336, 235, 2))
db.session.add(Room('Regina', 'Design/UX/Finance', 9, 351, 239, 2))
db.session.add(Room('Lovelace', 'Design/UX/Finance', 12, 433, 280, 2))
db.session.add(Room('Turing', 'Design/UX/Finance', 10, 394, 250, 2))
db.session.add(Room('Bob', 'Design/UX/Finance', 10, 378, 241, 2))
db.session.add(Room('Erdos', 'Design/UX/Finance', 10, 372, 216, 2))
db.session.add(Room('ContentArranger', 'Support/Marketing', 20, 402, 484, 1))
db.session.add(Room('EagleTransition', 'Support/Marketing', 20, 417, 495, 1))
db.session.add(Room('UserCell', 'Support/Marketing', 18, 373, 441, 1))
db.session.add(Room('AbstractElement', 'Support/Marketing', 18, 393, 450, 1))
db.session.add(Room('Please', 'Support/Marketing', 18, 348, 427, 1))
db.session.add(Room('Workshop', 'House of ideas', 13, 159, 758, 0))
db.session.add(Room('Geographer', 'Little Prince', 7, 231, 315, 2))
db.session.add(Room('Asteroid b-612', 'Little Prince', 7, 252, 301, 2))
db.session.add(Room('Elephant', 'Little Prince', 7, 249, 336, 2))
db.session.add(Room('Lamplighter', 'Little Prince', 7, 213, 324, 2))
db.session.add(Room('Rose', 'FOX', 1, 175, 429, 2))
db.session.add(Room('Baobab', 'FOX', 1, 141, 451, 2))
db.session.add(Room('Cinema', 'FOX', 1, 165, 423, 2))
db.session.add(Room('Totoro', 'Bento', 14, 67, 584, 1))
db.session.add(Room('Sangaku', 'Bento', 17, 73, 627, 1))
db.session.add(Room('Donkey Kong', 'Bento', 14, 88, 612, 1))
db.session.add(Room('Fuji', 'Bento', 16, 162, 642, 1))
db.session.add(Room('Stretch', 'Values', 30, 132, 252, 3))

db.session.commit()

Room.query.all()


