from app import Vaikas, Tevas, db

v1 = Vaikas("Vaikas", "Vaiksonas")

t1 = Tevas("Tevas", "Patevis", 1)

db.session.add_all([v1, t1])
db.session.commit()

vaikai = Vaikas.query.all()
print(dir(vaikai[0]))