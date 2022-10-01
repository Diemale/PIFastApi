#Acá creo clases que heredan de la clase retornada con declarative_base() en database.py (guardado en ls variable Base)
# de esta manera se crean los sqlalchemy models (model = class)

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float,Date
from sqlalchemy.orm import relationship, backref

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(150), unique=True, index=True)
    hashed_password = Column(String(150))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), index=True)
    description = Column(String(150), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Constructor(Base):
     __tablename__ = "constructor"

     constructorId  = Column(Integer, primary_key=True, index=True)
     nameConstructor = Column(String(150), index=True)
     nationality  =  Column(String(150), index=True)

     # Formateo la data sino el print solo muestra la posición en memoria donde se almacena el objeto
     # No cambia en nada el funcionamiento de mi clase, sirve solo para imprimirla
     def __repr__(self):
        return "Constructor(constructorId='{self.constructorId}', " \
        "nameConstructor='{self.nameConstructor}', " \
        "nationality='{self.nationality})'".format(self=self)



class Circuit(Base):
    __tablename__ = "circuit"

    circuitId  = Column(Integer, primary_key=True, index=True)
    circuitName = Column(String(150), index=True)
    location  =  Column(String(150), index=True)
    country	= Column(String(75), index=True)
    lat  = Column(Float, index=True)
    lng  = Column(Float, index=True)
    alt = Column(Integer, index=True)

    def __repr__(self):
        return "Circuito(circuitId='{self.circuitId}', " \
        "circuitName='{self.circuitName}', " \
        "location='{self.location}', " \
        "country='{self.country}', " \
        "lat='{self.lat}', " \
        "lng='{self.lng}', " \
        "alt='{self.alt})'".format(self=self)

class Driver(Base):
    __tablename__ = "driver"

    driverId  = Column(Integer, primary_key=True, index=True)
    driverNumber = Column(String(8), index=True)
    driverName	= Column(String(75), index=True)
    dob = Column(Date, index=True)
    nationality =  Column(String(100), index=True)

    def __repr__(self):
        return "Driver(driverId='{self.driverId}', " \
        "driverNumber='{self.driverNumber}', " \
        "driverName='{self.driverName}', " \
        "dob='{self.dob}', " \
        "nationality='{self.nationality})'".format(self=self)

   # owner = relationship("User", back_populates="items")

class Race(Base):
    __tablename__ = "race"

    raceId  = Column(Integer, primary_key=True, index=True)
    raceYear = Column(Integer, index=True)
    roundNumber = Column(Integer, index=True)
    circuitId = Column(Integer, ForeignKey("circuit.circuitId"), index=True)
    raceName = Column(String(100), index=True)
    raceDate = Column(Date, index=True)

    def __repr__(self):
        return "Race(raceId='{self.raceId}', " \
                "raceYear='{self.raceYear}', " \
                "roundNumber='{self.roundNumber}', " \
                "circuitId='{self.circuitId}', " \
                "raceName='{self.raceName}', " \
                "raceDate='{self.raceDate})'".format(self=self)

    # El backref=backref(...) es para relaciones 1 to many
    #circuit = relationship("Circuit", backref=backref("race", order_by=raceId))



class Result(Base):
    __tablename__ = "result"

    resultId  = Column(Integer, primary_key=True, index=True)
    raceId = Column(Integer, ForeignKey("race.raceId"), index=True)
    driverId = Column(Integer, ForeignKey("driver.driverId"), index=True)
    constructorId = Column(Integer, ForeignKey("constructor.constructorId"), index=True)
    resultNumber = Column(String(5), index=True)
    grid = Column(Integer, index=True)
    positionOrder	 = Column(Integer, index=True)
    points = Column(Float, index=True)
    laps = Column(Integer, index=True)
    raceTime = Column(String(12), index=True)
    miliseconds = Column(String(12), index=True)
    fastestLap = Column(String(5), index=True)
    rankP = Column(String(5), index=True)
    fastestLapTime = Column(String(12), index=True)
    fastestLapSpeed = Column(String(12), index=True)
    statusId = Column(Integer, index=True)


    def __repr__(self):
        return "Result(resultId='{self.resultId}', " \
             "raceId='{self.raceId}', " \
            "driverId='{self.driverId}', " \
             "constructorId='{self.constructorId}', " \
            "resultNumber='{self.resultNumber}', " \
            "grid='{self.grid}', " \
            "positionOrder='{self.positionOrder}', " \
             "points='{self.points}', " \
            "laps='{self.laps}', " \
            "raceTime='{self.raceTime}', " \
            "miliseconds='{self.miliseconds}', " \
            "fastestLap='{self.fastestLap}', " \
            "rankP='{self.rankP}', " \
            "fastestLapTime='{self.fastestLapTime}', " \
            "fastestLapSpeed='{self.fastestLapSpeed}', " \
            "statusId='{self.statusId})'".format(self=self)

    # El backref=backref(...) es para relaciones 1 to many
    #race = relationship("Race", backref=backref('result', order_by=resultId))
   # driver = relationship("Driver", backref=backref('result', order_by=resultId))
    #constructor = relationship("Constructor", backref=backref('result', order_by=resultId))

    #La línea de abajo establece una relación uno a uno
    #race = relationship("Race", uselist=False)

#tablaForanea = relationship("ClaseForanea", backref=backref("estatabla"... = PKdeEstaTabla)


