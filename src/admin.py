import os
from flask_admin import Admin
from models import db, User,People,Planet,Favorite_people,Favorite_planet
from flask_admin.contrib.sqla import ModelView
# importamos os para interactuar con el sistema operativo
# importamos flask_admin extension para la aplicacion de Flask
# importamos models para las definiciones de clase User, People, Planet, Favorite_people y Favorite_planet


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')
# setup_admin: Función que configura y agrega el panel de administración a la aplicación Flask.
# app.secret_key: Configura la clave secreta de la aplicación Flask, que se utiliza para proteger cookies y otros datos sensibles.
# os.environ.get('FLASK_APP_KEY', 'sample key'): Obtiene la clave secreta desde las variables de entorno o utiliza una clave de muestra si no está disponible.
# app.config['FLASK_ADMIN_SWATCH'] = 'cerulean': Configura el tema visual del panel de administración.
# admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3'): Crea una instancia de la clase Admin con el nombre "4Geeks Admin" y el modo de plantilla 'bootstrap3'.
    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Favorite_people, db.session))
    admin.add_view(ModelView(Favorite_planet, db.session))
# admin.add_view(ModelView(Modelo, db.session)): Agrega vistas para cada modelo a la interfaz de administración. Estas vistas permiten la administración y visualización de los registros de cada modelo.


    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))