from app import db, Message

db.create_all()  # sukurs mūsų lentelę DB

# Iš karto inicijuosime testams keletą įrašų:
jonas = Message('Jonas', 'jonas@mail.comm', 'Kažkoks labai rimtas atsiliepimas.', '861234569')
antanas = Message('Antanas', 'antanas@mail.ltm', 'Antano nuomonė labai svarbi.', '7554913822')
juozas = Message('Juozas', 'juozukas@friends.ltm', 'Aš labai piktas, nes blogai.', '12345629235')
bronius = Message('Bronius', 'bronka@yahoo.comm', 'Aš tai linksmas esu, man patinka.', '23168494623')

# Pridėsime šiuos veikėjus į mūsų DB
db.session.add_all([jonas, antanas, juozas, bronius])
# .commit išsaugo pakeitimus
db.session.commit()

print(jonas.id)
print(antanas.id)
print(bronius.id)
print(juozas.id)
