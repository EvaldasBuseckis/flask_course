from app import db, Message

# all_messages = Message.query.all()

message_antanas = Message.query.filter_by(name='Antanas')
print(message_antanas.message())