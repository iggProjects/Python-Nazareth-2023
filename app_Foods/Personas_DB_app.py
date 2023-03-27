#  https://github.com/chekulhan/python101/blob/main/sqlalchemy_app.py
#  https://www.digitalocean.com/community/tutorials/how-to-query-tables-and-paginate-data-in-flask-sqlalchemy

from flask import Flask, request, render_template, redirect, url_for

from flask_sqlalchemy import *
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Persona(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    nombre     = db.Column(db.String(30), nullable=False)
    apellido   = db.Column(db.String(30), nullable=False)
    ciudad     = db.Column(db.String(30), nullable=False)
    #fecha_ncto = db.Column(db.Date(), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    jon = Persona()
    jon.nombre = "JON"
    jon.apellido = "Jackson"
    jon.ciudad = "Caracas"
    #jon.fecha_ncto = "20/02/1923"

    igg = Persona()
    igg.nombre = "IGG"
    igg.apellido = "Luciano"
    igg.ciudad = "Johannesburgo"
    #igg.fecha_ncto = "20/02/1953"
    
    db.session.add_all([jon,igg])
    db.session.commit()

    personas = Persona.query.all()

    return render_template('index.html', personas=personas)    


if __name__=="__main__":
    app.run(debug=True)