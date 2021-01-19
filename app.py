from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "adoptionsareawesome"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def pet_list():
    """ List all the pets from adoption database """
    pets = Pet.query.all()
    return render_template("home.html", pets = pets)

@app.route("/add", methods = ['GET', 'POST'])
def add_new_pet():
    """Display form to add a new pet"""
    form = AddPet()
    if form.validate_on_submit():
        name = form.name.data 
        species = form.species.data 
        url = form.url.data 
        age = form.age.data 
        notes = form.notes.data 
        flash(f"Created a new pet for adoption!")
        return redirect('/')
    else:
        return render_template("add.html", form=form)

@app.route("/<int:id>", methods = ['GET', 'POST'])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = EditPet(obj = pet)

    if form.validate_on_submit():
        pet.name = form.name.data    
        pet.species = form.species.data 
        pet.url = form.url.data 
        pet.age = form.age.data 
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template("edit.html", form = form)
