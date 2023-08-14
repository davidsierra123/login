from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/entrada_salida'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "entrada_salida1"

db = SQLAlchemy(app)

ma = Marshmallow(app)