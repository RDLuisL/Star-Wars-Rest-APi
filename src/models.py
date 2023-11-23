from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# importamos el framework de Flask
# importamos la libreria flask_sqlalchemy desde Flask

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# Este modelo representa a un usuario con campos como id, email, password, y is_active.
# La función __repr__ proporciona una representación de cadena del objeto para facilitar la depuración.
# La función serialize devuelve una representación serializada del objeto que puede ser convertida
#  a JSON.


class People (db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), unique=False, nullable=False)
    gender=db.Column(db.String(30), unique=False, nullable=False)
    hair_color=db.Column(db.String(25), unique=False, nullable=False)
    skin_color=db.Column(db.String(25), unique=False, nullable=False)

    def __repr__(self):
            return '<People %r>' % self.name

    def serialize(self):
            return {
                "id": self.id,
                "Name": self.name,
                "Gender": self.gender,
                "Hair color": self.hair_color,
                "Skin color": self.skin_color,

                # do not serialize the password, its a security breach
            }
# Este modelo representa a un personaje (People) con campos como id, name, gender, hair_color, y 
# skin_color.

class Planet (db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), unique=False, nullable=False)
    population=db.Column(db.String(30), unique=False, nullable=False)
    terrain=db.Column(db.String(25), unique=False, nullable=False)
    climate=db.Column(db.String(25), unique=False, nullable=False)
    # modificado este tramo

    def __repr__(self):
            return '<Planet %r>' % self.name
            
    def serialize(self):
            return {
                "id": self.id,
                "Name": self.name,
                "Population":self.population,
                "Climate":self.climate,

                # do not serialize the password, its a security breach
            }
# Este modelo representa a un planeta (Planet) con campos como id, name, population, terrain, y climate.

class Favorite_people(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id') )
    user_name =  db.Column(db.String(120), db.ForeignKey('user.email'))
    
    rel_user = db.relationship('User')
    rel_personaje = db.relationship('People')

    def __repr__(self):
        return '<Favorite_people %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "people_id": self.people_id,
            "email": self.email
            # do not serialize the password, its a security breach
        }
# Este modelo representa la relación entre usuarios y personajes favoritos (Favorite_people).

class Favorite_planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id') )
    user_name =  db.Column(db.String(120), db.ForeignKey('user.email'))

    rel_user = db.relationship('User')
    rel_planet = db.relationship('Planet')

    def __repr__(self):
        return '<Favorite_planet %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "Planet_id": self.planet_id,
            "email": self.email
            # do not serialize the password, its a security breach
        }
# Este modelo representa la relación entre usuarios y planetas favoritos (Favorite_planet).
