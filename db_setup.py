from roomie import db
db.create_all()

from roomie import Room

db.session.add(Room('Spline', 'Talent/DLR/Community', 25, 655, 230, 3))
db.session.add(Room('Cat\'s cradle', 'Talent/DLR/Community', 25, 655, 190, 3))
db.session.add(Room('Hypercube', 'Talent/DLR/Community', 25, 655, 150, 3))
db.session.add(Room('Fractal', 'Talent/DLR/Community', 28, 657, 343, 3))
db.session.add(Room('Icosidodecahedron', 'Talent/DLR/Community', 25, 739, 117, 3))
db.session.add(Room('Eames', 'Design/UX/Finance', 9, 622, 117, 2))
db.session.add(Room('Regina', 'Design/UX/Finance', 9, 653, 117, 2))
db.session.add(Room('Lovelace', 'Design/UX/Finance', 12, 671, 381, 2))
db.session.add(Room('Turing', 'Design/UX/Finance', 10, 669, 229, 2))
db.session.add(Room('Bob', 'Design/UX/Finance', 10, 669, 180, 2))
db.session.add(Room('Erdos', 'Design/UX/Finance', 10, 739, 117, 2))
db.session.add(Room('ContentArranger', 'Support/Marketing', 20, 647, 343, 1))
db.session.add(Room('EagleTransition', 'Support/Marketing', 20, 647, 384, 1))
db.session.add(Room('UserCell', 'Support/Marketing', 18, 661, 180, 1))
db.session.add(Room('AbstractElement', 'Support/Marketing', 18, 661, 243, 1))
db.session.add(Room('Please', 'Support/Marketing', 18, 661, 152, 1))
db.session.add(Room('Workshop', 'House of ideas', 13, 164, 182, 0))
db.session.add(Room('Geographer', 'Little Prince', 7, 433, 126, 2))
db.session.add(Room('Asteroid b-612', 'Little Prince', 7, 488, 126, 2))
db.session.add(Room('Elephant', 'Little Prince', 7, 420, 240, 2))
db.session.add(Room('Lamplighter', 'Little Prince', 7, 374, 126, 2))
db.session.add(Room('Rose', 'FOX', 1, 211, 381, 2))
db.session.add(Room('Baobab', 'FOX', 1, 106, 381, 2))
db.session.add(Room('Cinema', 'FOX', 1, 211, 336, 2))
db.session.add(Room('Totoro', 'Bento', 14, 160, 113, 1))
db.session.add(Room('Sangaku', 'Bento', 17, 90, 216, 1))
db.session.add(Room('Donkey Kong', 'Bento', 14, 150, 216, 1))
db.session.add(Room('Fuji', 'Bento', 16, 224, 334, 1))
db.session.add(Room('Stretch', 'Values', 30, 205, 372, 3))

db.session.commit()

Room.query.all()


