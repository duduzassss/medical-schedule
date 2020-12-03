from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# lm = LoginManager()
# lm.init_app(app)

from app.models import models
# Importando no flask os controllers depois da instancia
# de app, pq precisamos que ela já esteja declarada, 
# pois usamos a variável app nos nossos módulos
from app.controllers.home import routes
# from app.controllers.auth import routes, forms
from app.controllers.medicos import routes, forms
from app.controllers.pacientes import routes, forms

