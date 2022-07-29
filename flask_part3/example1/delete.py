from app import Message, db


jonas = Message.query.get(3)
db.session.delete(jonas)
db.session.commit()
print(Message.query.all())

