""" Fastapi es un framework microweb que me permite crear  API's que me permite conectar data a través del protocolo
 HTTP"""

from fastapi import Depends, FastAPI, HTTPException, Path
# from sqlalchemy import func # sirve para utilizar funciones de agregación de SQL
from sqlalchemy.orm import Session, sessionmaker
import crud, models, schemas
###from database import  engine, Session #SessionLocal
from enum import Enum

class nombreModelo(str):
    conductor = "driver"
    circuito = "circuit"
    carrera = "race"
    escuderia = "constructor"
    resultado = "result"

class Pedidos(str,Enum):
    maxCarrerasPorAnio = "maxCarreras"
    masGanador = "maximoGanador"
    circuitoMasApariciones = "Circuito con más carreras"
    pilotoMasPuntosEscuderiaBRT_USA = "piloto más ganador con escudería inglesa o americana"
    altitudPromedio = "altitudPromedio"

# crear todas las tablas en la base de datos definidas por el engine
#models.Base.metadata.create_all(bind=engine)

#Creo un objeto FastAPI(), esto es la aplicación que voy a utilizar

# crear mi sesión para utilizar la base de datos
#session = Session()

app = FastAPI()

@app.get("/queries/{nombre_query}")
async def get_query(nombre_query: Pedidos):
    if nombre_query is Pedidos.maxCarrerasPorAnio:
        return crud.anio_con_mas_GPs()
    elif nombre_query is Pedidos.masGanador:
        return crud.obtener_pilotos_mas_ganadores()
    elif nombre_query is Pedidos.circuitoMasApariciones:
        return crud.circuito_mas_recorrido()
    elif nombre_query is Pedidos.pilotoMasPuntosEscuderiaBRT_USA:
        return crud.piloto_escuderia_ing_usa()
    else:
        return crud.obtenerPromedio(models.Circuit, models.Circuit.alt)


@app.get("/modelos/{nombre_modelo}")
async  def get_modelo(nombre_modelo: nombreModelo):
    if nombre_modelo is nombreModelo.conductor:
        return {"nombre_modelo": nombre_modelo, "mensaje": "Modelo Driver"}
    if nombre_modelo.value == "circuit":
        return {"nombre_modelo": nombre_modelo, "mensaje": "Modelo Circuit"}
    if nombre_modelo is nombreModelo.carrera:
        return {"nombre_modelo": nombre_modelo, "mensaje": "Modelo Race"}
    if nombre_modelo is nombreModelo.escuderia:
        return {"nombre_modelo": nombre_modelo, "mensaje": "Modelo Constructor"}
    if nombre_modelo is nombreModelo.resultado:
        return {"nombre_modelo": nombre_modelo, "mensaje": "Modelo Result"}

@app.get("/altitudPromedio")
async def altitudPromedio():
    return

@app.get("/operaciones")
async def realizarOperacion(modelo,columna,operacion):
    return





# Levantar la data que está en la base datos original, esto es posible gracias al mapeo que SQLALCHEMY realiza con los
# modelos ORM (Clases/tablas) declarados en el archivo model. Los datos son devueltos como una lista de objetos
# CUIDADO!!! Estos datos tienen una conexión directa con la base de datos. Por lo tanto, cualquier cambio que se realice
# sobre estos se verá reflejado en la base de datos original.
"""constructor = session.query(models.Constructor).all()
circuit = session.query(models.Circuit).all()
driver = session.query(models.Driver).all()
race = session.query(models.Race).all()
#result = session.query(models.Result).all()

print(len(constructor))
print(constructor)
print(session.query(models.Constructor.nameConstructor, models.Constructor.nationality).first())
print(len(circuit))
#print(circuit)

#print(len(driver))
#print(driver)

#print(len(race))
#print(race)

#print(len(result))
#print(result)
for escuderia in session.query(models.Constructor).order_by(models.Constructor.nationality.desc()).limit(5):
    print('{} : {}'.format(escuderia.nameConstructor, escuderia.nationality))

alturaPromedio = session.query(func.avg(models.Circuit.alt)).scalar()
alturaPromedio2 = session.query(func.avg(models.Circuit.alt)).first()
alturaPromedio3 = session.query(func.avg(models.Circuit.alt).label('alturaPromedio3Label')).first()
print(alturaPromedio)
print(alturaPromedio2)
print(alturaPromedio3)

print(alturaPromedio3.keys())
print(alturaPromedio3.alturaPromedio3Label)"""

# Dependency
#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()






# Para tener una mejor interacción con el usuario necesito que se puedan realizar requests de un mayor tamaño, como por
# un objeto creado con Python. Para esto podemos usar el protocolo Post, y vamos a usar Pydantic para validar la data
# de las requests (Lo manejo en el archivo schemas)


# Debajo estoy pidiendo que app utilice un método del protocolo HTTP (post, get, etc) y use las rutas pasadas como
# parámetro. Para poder utilizarlas necestito una base de datos, de eso me encargo en el archivo database.

"""@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
"""
