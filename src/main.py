"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,People,Planet,Favorite_people,Favorite_planet 
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    all_user = User.query.all()
    serializados = list(map(lambda user: user.serialize(), all_user))
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/People', methods=['GET'])
def get_people():
    all_people = People.query.all()
    all_people = list( map(lambda people:people.serialize(), all_people))
    return jsonify(all_people)

@app.route('/People/<int:people_id>', methods=['GET'])
def solo_people(people_id):
    solo = People.query.get(people_id)
    print(solo)
    return jsonify(solo.serialize())


@app.route('/Planet', methods=['GET'])
def get_planet():
    all_planet = Planet.query.all()
    print(all_planet)
    all_planet = list( map(lambda planet:planet.serialize(), all_planet))
    return jsonify(all_planet)

@app.route('/Planet/<int:planet_id>', methods=['GET'])
def solo_planet(planet_id):
    planetita = Planet.query.get(planet_id)
    print(planetita)
    return jsonify(planetita.serialize())

@app.route('/user/Favorite_people', methods=['GET'])
def get_people_favorite():
    people_fav = Favorite_people.query.all()
    print(people_fav)
    people_fav = list( map(lambda people_fav:peole_fav.serialize(), people_fav))
    return jsonify(people_fav)

@app.route('/user/Favorite_planet', methods=['GET'])
def get_planet_favorite():
    planet_fav = Favorite_planet.query.all()
    print(planet_fav)
    planet_fav = list( map(lambda planet_fav:planet_fav.serialize(), planet_fav))
    return jsonify(planet_fav)

@app.route('/People/Favorite_people/<int:people_id>', methods=['POST'])
def add_people_fav():
    revisar_personaje= People.query.get(people_id)
    user = User.query.get(1)
    if (revisar_personaje):
        new_fav = Favorite_people()
        new_fav_email = user.email
        new_fav_people_id = people_id
        db.session.add(new_fav)
        db.session.commit()
        return "registrado maestro jedi"
    else:
        raise APIException("No existe el personaje", status_code=404)

@app.route('/Planet/Favorite_planet/<int:planet_id>', methods=['POST'])
def add_planet_fav():
    revisar_planeta= Planet.query.get(planet_id)
    user = User.query.get(1)
    if (revisar_planet):
        new_fav = Favorite_planet()
        new_fav_email = user.email
        new_fav_planet_id = planet_id
        db.session.add(new_fav)
        db.session.commit()
        return "planeta registrado"
    else:
        raise APIException("No existe el planeta viajero", status_code=404)

@app.route('/People/Favorite_people/<int:people_id>', methods=['DELETE'])
def delete_people_fav(people_id):
    eliminar_people = Favorite_people.query.filter_by(people_id=people_id).first()
    if (eliminar_people):
         db.session.delete(eliminar_people)
         db.session.commit()
         return "Personaje eliminado!"
    else: raise APIException("No logro eliminar el personaje!", status_code=404)
 
@app.route('/Planet/Favorite_planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_fav(planet_id):
    eliminar_planet = Favorite_planet.query.filter_by(planet_id=planet_id).first()
    if (eliminar_planet):
         db.session.delete(eliminar_planet)
         db.session.commit()
         return "Planeta eliminado!"
    else: raise APIException("No logro eliminar el planeta!", status_code=404)
 
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
