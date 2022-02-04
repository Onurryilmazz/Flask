from app import db
from app import Item


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