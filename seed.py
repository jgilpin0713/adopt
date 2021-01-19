
from models import Pet, db
from app import app

#Create tables
db. drop_all()
db.create_all()

#id: auto-incrementing integer
#name: text, required
#species: text, required
#photo_url: text, optional
#age: integer, optional
#notes: text, optional
#available: true/false, required, should default to available

geoffrey = Pet(name = "Geoffrey", species = "giraffe", photo_url ="https://cdn.shopify.com/s/files/1/1685/2975/products/FC3549_working_1024x1024.jpg?v=1522162248",
                 age = 72, notes = "Toys R' Us!", available = False)
spot = Pet(name = "Spot", species = "cat", age = 20)
lizzy = Pet(name = "Lizzy", species = "cat", age= 22)
speedy = Pet(name = "Speedy", species = "cat", age =21)
tom = Pet(name = "Tom", species = "cat", photo_url ="https://img.theweek.in/content/dam/week/leisure/society/images/2018/3/17/tom-and-jerry.jpg",
                  age = 80, notes = "Best friend is a mouse", available = False)
jerry = Pet(name = "Jerry", species = "mouse", photo_url = "https://img.theweek.in/content/dam/week/leisure/society/images/2018/3/17/tom-and-jerry.jpg",
                  age = 80, notes = "Comes with a Cat!", available = False)
bambi = Pet(name = "Bambi", species = "deer", photo_url = "https://static.highsnobiety.com/thumbor/0vOuDhcDUk9fFEjSYenDj-3CW1U=/1600x1067/static.highsnobiety.com/wp-content/uploads/2020/01/25123443/disney-bambi-live-action-remake-01.jpg",
                  age = 2, notes = "Live Action!!")

db.session.add_all([geoffrey, spot, lizzy, speedy, tom, jerry, bambi])
db.session.commit()
