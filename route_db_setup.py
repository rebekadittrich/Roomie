from roomie import db
db.create_all()

from roomie import Route

db.session.add(Route(1, 2, 'Menj le a lepcson, vegig a folyoson es fel'))
db.session.add(Route(1, 3, 'Fordulj balra aztan kettot jobbra'))
db.session.add(Route(1, 4, 'Lifttel ket szintet le'))
db.session.add(Route(1, 5, 'Hmmmm'))

db.session.commit()

Route.query.all()