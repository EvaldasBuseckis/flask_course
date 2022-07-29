from app import Message, db


antanas = Message.query.get(2)
antanas.email = 'blogas.zmogus@lrs.lt'
db.session.add(antanas)
db.session.commit()
print(Message.query.all())