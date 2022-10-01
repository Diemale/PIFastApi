from sqlalchemy.orm import Session
from sqlalchemy import text, func # sirve para utilizar funciones de agregación de SQL
from database import  engine, Session
import models, schemas



# crear mi sesión para utilizar la base de datos
session = Session()

# Levantar la data que está en la base datos original, esto es posible gracias al mapeo que SQLALCHEMY realiza con los
# modelos ORM (Clases/tablas) declarados en el archivo model. Los datos son devueltos como una lista de objetos
# CUIDADO!!! Estos datos tienen una conexión directa con la base de datos. Por lo tanto, cualquier cambio que se realice
# sobre estos se verá reflejado en la base de datos original.
# Las líneas de abajo se corresponden con un select * from mi_Tabla

constructor = session.query(models.Constructor).all()
circuit = session.query(models.Circuit).all()
driver = session.query(models.Driver).all()
race = session.query(models.Race).all()
result = session.query(models.Result).all()


##############################################   tutorial sqlalchemy   #################################################


########################################################################################################################



def obtener_pilotos_mas_ganadores():
    stmt = text("SELECT d.driverName, g.ganadas FROM ((select driverId, count(positionOrder) as ganadas from result "
            "WHERE positionOrder = 1 GROUP BY driverId order by ganadas desc , driverId ) as g join driver d on "
            "(g.driverId = d.driverId))")
    result = session.execute(stmt)
    mg = result.first()
    return "El piloto más ganador es " + str(mg[0]) + " con " + str(mg[1]) + " victorias."

def anio_con_mas_GPs():
    stm = text("select count(raceId) as cant, raceYear from race group by raceYear order by cant desc")
    result = session.execute(stm)
    mGPs = result.first()
    return "El año con mayor cantidad de grandes premios fue el año " + str(mGPs[1]) + " con "+ str(mGPs[0]) + " carreras."


def circuito_mas_recorrido():
    stmt = text("select count(r.raceId) as total, c.circuitName from ((select raceId, circuitId from race) as r "
               "join( select circuitId, circuitName from circuit) as c on (r.circuitId = c.circuitId))"
               "group by c.circuitName order by total desc, circuitName limit 1")

    result = session.execute(stmt)
    mr = result.all()
    # en caso de devolver más de una muestra se puede acceder a los elementos particulares con notación de matrices
    return "El circuito con mayor presencia en F1 es el " + str(mr[0][1]) + " con " + str(mr[0][0]) + " apariciones."


def piloto_escuderia_ing_usa():
    stmt = text("select d.driverName, sum(r.points) as tp, c.nationality from driver d "
            "join result r on(d.driverId = r.driverId) "
            "join constructor c on(r.constructorId = c.constructorId) "
            "group by d.driverName, c.nationality having (nationality = 'British' or nationality = 'American') " \
            "order by tp desc limit 10")

    result = session.execute(stmt)
    mr = result.first()
    return "El piloto que cosechó más puntos con una escudería estadounidense o británica es " + mr[0] +\
            " con " + str(int(mr[1])) + " puntos."



stmt = text("select d.driverName, sum(r.points) as tp, c.nationality from driver d "
            "join result r on(d.driverId = r.driverId) "
            "join constructor c on(r.constructorId = c.constructorId) "
            "group by d.driverName, c.nationality having (nationality = 'British' or nationality = 'American') " \
            "order by tp desc limit 10")

result = session.execute(stmt)
mr = result.all()
for elemento in mr:
    print(elemento[0], int(elemento[1]))
#print(mr.driverName)
print(mr)



def obtenerPrimerItem():
    return session.query()

def obtenerPromedio(modeloPedido, columnaDelModelo):
    print(modeloPedido, columnaDelModelo + "#########################################################################")
    return session.query(func.avg(models.modeloPedido.columnaDelModelo))
#####################################################################################################################


