from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

'mysql+pymysql://<username>:<password>@<host>/<dbname>'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://tesselj2:tquaJgBKa1Ow0t5L@oege.ie.hva.nl/ztesselj2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)