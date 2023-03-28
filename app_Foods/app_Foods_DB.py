#  https://github.com/chekulhan/python101/blob/main/sqlalchemy_app.py
#  https://www.digitalocean.com/community/tutorials/how-to-query-tables-and-paginate-data-in-flask-sqlalchemy

from flask import Flask, request, render_template, redirect, url_for

from flask_sqlalchemy import *
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'foods.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Plato(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    tipo       = db.Column(db.String(10), nullable=False)
    nombre     = db.Column(db.String(30), nullable=False)
    precio     = db.Column(db.Float, nullable=False)
    disp       = db.Column(db.Integer, nullable=False, default=1)
    

with app.app_context():
    db.create_all()

@app.route("/")

def index():
    """
    plato01 = Plato()
    plato01.tipo = "Entrada"
    plato01.nombre = "Ensalada Mixta"
    plato01.precio = 4
    plato01.disp = 1    

    plato02 = Plato()
    plato02.tipo = "Entrada"
    plato02.nombre = "Ensalada Rusa"
    plato02.precio = 4
    plato02.disp = 1    

    plato03 = Plato()
    plato03.tipo = "Ppal"
    plato03.nombre = "Pasta al pesto"
    plato03.precio = 6
    plato03.disp = 1    

    plato04 = Plato()
    plato04.tipo = "Postre"
    plato04.nombre = "tarta queso"
    plato04.precio = 3
    plato04.disp = 1    

    
    db.session.add_all([plato01,plato02,plato03,plato04])
    db.session.commit()
    """
    menu_del_dia = Plato.query.all()
    
    #menu_del_dia.sort(key=get_tipo)
    #print(f"menu del día: {menu_del_dia} | length: {len(menu_del_dia)}  | type: {type(menu_del_dia)}")
    #print(f"plato 1:  {menu_del_dia[1].nombre}") 
    entrada = []
    ppal   = []
    postre  = []
    errores = []

    for i in range(len(menu_del_dia)):
        if menu_del_dia[i].tipo == 'Entrada':
            entrada.append(menu_del_dia[i])
        elif menu_del_dia[i].tipo == 'Ppal':
            ppal.append(menu_del_dia[i])
        elif menu_del_dia[i].tipo == 'Postre':
            postre.append(menu_del_dia[i])
        else:
            errores.append(menu_del_dia[i])                                                                                                                                                                                                 
            print('upsssss somthing is wrong... 🙄')  

    #print(f"plato entrada:  {entrada[1].nombre}")  

    for i in range(len(entrada)):
        entrada[i].id = i +1

    for i in range(len(ppal)):
        ppal[i].id = i +1

    for i in range(len(postre)):
        postre[i].id = i +1


    return render_template('index.html', entrada=entrada, ppal=ppal, postre=postre)

@app.route('/login',methods=['GET', 'POST'])
def login():      
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            #return redirect(url_for('home'))
            return render_template('home_admin.html')
        
    return render_template('login.html', error=error)

@app.route('/home_admin')
def home_admin():
    return render_template('home_admin.html')

@app.route('/reg_matrix')
def reg_matrix():    
    platos = Plato.query.all()
    return render_template('reg_matrix.html', platos=platos)

@app.route('/reg_insert',methods=['POST','GET'])
def reg_insert():
    if request.method == 'POST':

        plato_nuevo = Plato()
        plato_nuevo.tipo = request.form['fTipo']
        plato_nuevo.nombre = request.form['fNombre']
        plato_nuevo.precio = request.form['fPrecio']
        plato_nuevo.disp = 1   

        print(plato_nuevo.nombre)

        db.session.add(plato_nuevo)
        db.session.commit()

        return redirect(url_for("reg_matrix"))
    
    return render_template('reg_insert.html')

@app.route('/reg_update/<string:uid>', methods=['POST','GET'])
def reg_update(uid):
    return render_template('reg_update.html')

@app.route('/reg_delete/<string:uid>', methods=['GET'])
def reg_delete(uid):  
    plato=Plato.query.get(uid)
    db.session.delete(plato)    
    db.session.commit()
    return render_template('reg_matrix.html')

if __name__=="__main__":
    app.run(debug=True)