from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea
from datetime import datetime, date

app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask

# La barra (el slash) se conoce como la pagina de inicio (pagina home).
# Vamos a definir para esta ruta, el comportamiento a seguir.
@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all() # Consultamos y almacenamos todas las tareas de la base de datos
    # Ahora en la variable todas_las_tareas se tienen almacenadas todas las tareas. Vamos a entregar esta variable al template index.html
    return render_template("index.html", lista_de_tareas=todas_las_tareas) # Se carga el template index.html

@app.route('/crear-tarea', methods=['POST'])
def crear():
    """La funcion crear recive los parametros necesarios para crear una entrada en la db de tareas
    pero antes comprueba algunos parametros para evitar errores"""

    fecha_limite_check = request.form.get('fecha_limite_tarea')

    if fecha_limite_check: #Checkeo si la fecha esta vacia para evitar errores al meter en SQLAlchemy
        try:
            fecha_limite_aft_check = datetime.strptime(fecha_limite_check,"%Y-%m-%d").date()
        except ValueError:
            return print("La fecha esta vacia")
    else:
        fecha_limite_aft_check = None

    # Tarea es un objeto de la clase Tarea (una instancia de la clase)
    tarea = Tarea(contenido=request.form['contenido_tarea'],
                  hecha=False,
                  categoria=request.form['categoria_tarea'],
                  fecha_limite=fecha_limite_aft_check,
                  limite_ok = False)
    # id no es necesario asignarlo manualmente, porque la primary key se genera automaticamente
    db.session.add(tarea) # Anyadir el objeto de Tarea a la base de datos
    db.session.commit() # Ejecutar la operacion pendiente de la base de datos
    check_fecha_limite() #Checkeamos las fechas para poner tarea.limite_ok a True o False
    return redirect(url_for('home')) # Esto nos redirecciona a la funcion home()

@app.route('/cambiar-crear-tarea', methods=['POST'])
def cambiar_crear():
    """La funcion cambiar_crear abre la pagina para crear tareas o crear_tarea.html"""
    return render_template("crear_tarea.html") # Se carga el template crear_tarea.html

@app.route('/vuelta-home', methods=['POST'])
def vuelta_home():
    """La funcion vuelta_home esta conectada a el boton cancelar o futuras funciones, esta funcion nos manda a la funcion home
    y a su vez a index.html"""
    return redirect(url_for('home'))

@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    """La funcion eliminar esta conectada son el boton de eliminar de cada tarea, al pulsar el boton el usuario,
    la funcion recibe la id de la tarea y la borra de la db"""
    tarea = db.session.query(Tarea).filter_by(id=int(id)).delete() # Se busca dentro de la base de datos,
                                                                   # aquel registro cuyo id coincida con el aportado por el parametro
                                                                   # de la ruta. Cuando se encuentra se elimina
    db.session.commit() # Ejecutar la operacion pendiente de la base de datos
    return redirect(url_for('home')) # Esto nos redirecciona a la funcion home() y si todo ha ido bien, al refrescar, la tarea eliminada
                                     # ya no aparecera en el listado

@app.route('/tarea-goto-modificar/<id>')
def tarea_goto_modificar(id):
    """La funcion tarea_goto_modificar recibe la id de la tarea a modificar y redirige al usuario a modificar_tarea.html
    donde podra modificar los parametros de la tarea que haya seleccionado"""
    tarea_a_modificar = db.session.query(Tarea).filter_by(id=int(id)).first() # Consultamos y almacenamos la tarea de la base de datos a modificar
    # Ahora en la variable todas_las_tareas se tienen almacenadas todas las tareas. Vamos a entregar esta variable al template index.html
    return render_template("modificar_tarea.html", modificar = tarea_a_modificar) # Se carga el template index.html

@app.route('/modificar-tarea', methods=['POST'])
def modificar():
    """La funcion modificar se utiliza en modificar_tarea.html, con esta funcion el usuario fuede modificar los parametros
    contenido, categoria y fecha limite segun su necesidad y modificar las tareas"""
    id = request.form['id-tarea']
    print(id)
    tarea = db.session.query(Tarea).get(id)
    print(tarea)
    fecha_limite_check = request.form.get('fecha_limite_tarea')

    if fecha_limite_check: #Checkeo si la fecha esta vacia para evitar errores al meter en SQLAlchemy
        try:
            fecha_limite_aft_check = datetime.strptime(fecha_limite_check,"%Y-%m-%d").date()
        except ValueError:
            return print("La fecha esta vacia")
    else:
        fecha_limite_aft_check = None
    tarea.contenido = request.form['contenido_tarea']
    tarea.categoria = request.form['categoria_tarea']
    tarea.fecha_limite = fecha_limite_aft_check
    db.session.commit() # Ejecutar la operacion pendiente de la base de datos
    check_fecha_limite() #Checkeamos las fechas para poner tarea.limite_ok a True o False
    return redirect(url_for('home')) # Esto nos redirecciona a la funcion home()

@app.route('/tarea-hecha/<id>')
def hecha(id):
    """La funcion hecha esta conectada al index.html, cuando el usuario pulsa en el boton de hecha se negara el estado de la variable,
    asi el usuario podra activar la variable hecha a su necesidad"""
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first() # Se obtiene la tarea que se busca
    tarea.hecha = not(tarea.hecha) # Guardamos en la variable booleana la tarea, su contrario
    db.session.commit() # Ejecutar la operacion pendiente de la base de datos
    check_fecha_limite() #Checkeamos las fechas para poner tarea.limite_ok a True o False
    return  redirect(url_for('home')) # Esto nos redirecciona a la funcion home()

def check_fecha_limite():
    """La funcion check_fecha_limite comprueba todas las fechas configuradas pra las tareas.
    Hay tres posibles casos, el primero la fecha esta a None ya que no tiene fecha configurada y la variable limite_ok quedara en False
    el segundo la fecha limite es menor que la fecha actual y la variable limite_ok se escribira en True
    el tercero la fecha limite es mayor o igual, en este caso se escribira False"""
    tarea_to_check = db.session.query(Tarea).all()
    for tareas in tarea_to_check:
        if tareas.fecha_limite: #Checkeo si la fecha esta vacia para evitar errores
            try:
                tareas.fecha_limite < fecha_hoy
            except ValueError:
                return print("La fecha esta vacia")
            else:
                if tareas.fecha_limite < fecha_hoy:
                    tareas.limite_ok = True
                else:
                    tareas.limite_ok = False
        else:
            tareas.limite_ok = False

if __name__ == '__main__':
    fecha_hoy = date.today() #Guardado en una variable la fecha de hoy para furutas comprobaciones
    db.Base.metadata.create_all(db.engine) # Creamos el modelo de datos
    check_fecha_limite() #Checkeamos las fechas para poner tarea.limite_ok a True o False
    app.run(debug=True) # El debug=True hace que cada vez que reiniciemos el servidor o modifiquemos codigo, el servidor de Flask se reinicie solo
