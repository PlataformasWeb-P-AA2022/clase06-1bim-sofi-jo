from sqlalchemy.orm import sessionmaker

from crear_base import Saludo
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo

miSaludo = Saludo()
miSaludo.mensaje = "Hola mundo desde SqlAlchemy y SQLite"


miSaludo2 = Saludo()
miSaludo2.mensaje = "Hola mundo dos desde SqlAlchemy y SQLite"

# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
session.add(miSaludo)
session.add(miSaludo2)

# se confirma las transacciones
session.commit()