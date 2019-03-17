from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Ce2U9zj5NVu9Cl4H"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://xnuagmajhaccqi:d50dbbbd5eba079f05050b14c879d9d934451304aefb5ae7681db686bf2d78b5@ec2-23-23-195-205.compute-1.amazonaws.com:5432/d7alrd3vk5e8gg"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views