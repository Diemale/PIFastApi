from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:**casancrenClasico28**@localhost:3306/piuno"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#Para conectar a la database, necesitamos crear un SQLAlchemy engine
# este engine crea una interface común a la base de datos para ejecutar sentencias de tipo SQL
# Por default sqlalchemy hace el encode en utf-8.
# Paso el path a la base de datos como parámetro, pymysql es una librería que me permite buscarla de forma automática
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Definir una clase Session con la configuración bind que me provee el módulo sessionmaker de sqlalchemy.
# Ya tengo la ruta de acceso, ahora falta iniciar una sesión en la base de datos, lo voy a hacer llamando
# (desde el archivo CRUD) al objeto sessionmaker que declaro abajo.
Session = sessionmaker(bind=engine)




#En SQLAlchemy ORM, vamos a definir una clase que hereda de la clase especial declarative_base.
#Esta clase combina un contenedor de  metadata y un mapper que mapea nuestra clase a la tabla de la base de datos
Base = declarative_base()
