import db
from sqlalchemy import Column, Integer, String, Boolean, Date

""""
Creamos una clase llamada Tarea
Esta clase va a ser nuestro modelo de datos de la tarea (el cual nos servira luego para la base de datos)
Esta clase va a almacenar toda la informacion referente a una tarea
"""

class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True) # Identificador unico de cada tarea (no puede haber dos tareas con el mismo id, por eso  es primary key)
    contenido = Column(String(200), nullable=False) #Contenido de la tarea, un texto maximo de 200 caracteres
    hecha = Column(Boolean) #Booleano que indica si una tarea ha sido hecha o no
    categoria = Column(String(100)) # Categoria de la tarea, un texto maximo de 100 caracteres
    fecha_limite = Column(Date) #Fecha limite en que la tarea ha de ser completada
    limite_ok = Column(Boolean) #Limite_ok se pondra a True cuando la fecha limite sea menor a la fecha actual

    def __init__(self, contenido, hecha, categoria, fecha_limite, limite_ok):
        #Recordemos que el id no es necesario crearlo manualmente, lo anyade la base de datos automaticamente
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria
        self.fecha_limite = fecha_limite
        self.limite_ok = limite_ok

    def __repr__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.categoria, self.fecha_limite, self.hecha, self.limite_ok)

    def __str__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.categoria, self.fecha_limite, self.hecha, self.limite_ok)