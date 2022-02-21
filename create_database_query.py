from market import app
from market.models import app
from market.models import db, Item, User

#Uygulama çalışırken aynı dizinde sırasıyla çalıştırılacak kodlar


db.create_all()

item1 = Item(name='Iphone10',price='500',barcode='846154104831',description='desc')
db.session.add(item1)
db.session.commit()

item2 = Item(name='Laptop',price='600',barcode='321154104169',description='desc2')
db.session.add(item2)
db.session.commit()


# db verilerini görmek için
for item in Item.query.all():
     item.name
     item.price
     item.description
     item.id
     item.barcode

#filtreleme 
for item in Item.query.filter_by(price=500):
     item.name

# version 2

db.drop_all()
db.create_all()
u1 = User(username='jsc',password_hash='123456',email_address='jsc@jsc.com')
db.session.add(u1)
db.session.commit()
User.query.all()
item1 = Item(name='Iphone10',price='800',barcode='123456789123',description='desc')
db.session.add(item1)
db.session.commit()
item2 = Item(name='Laptop',price='1000',barcode='683456789123',description='desc2')
db.session.commit()
db.session.add(item2)
db.session.commit()
Item.query.all()


