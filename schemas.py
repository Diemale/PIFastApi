"""Pydantic me permite validar de manera automática la data. Por ejemplo los objetos que vayan a ser consumidos por una
post request serán validados por esta librería, ahorrándonos el trabajo de escribir código de validación de los inputs
del usuario"""

from pydantic import BaseModel, Field


class Circuito(BaseModel):
    circuitId: int = Field(gt=0)
    circuitName:str  = Field(min_length=1, max_length=150)
    country: str = Field(min_length=1, max_length=75)
    lat: float = Field(gt=-90.0, lt=90.0) #Como el greater than, less than de assembler
    long: float = Field(gt=-180.0, lt=180.0)
    alt: int   = Field(gt=-100, lt=10000)


class Constructor(BaseModel):
     constructorId: int  = Field(gt=0, lt= 500000)
     nameConstructor: str = Field(min_length=1, max_length=150)
     nationality:str = Field(min_length=1, max_length=150)


class Driver(BaseModel):
    driverId:int = Field(gt=0, lt= 500000)
    driverNumber:str =  Field(min_length=1, max_length=8)
    driverName: str	= Field(min_length=1, max_length=75)
    dob: str = Field(min_length=1, max_length=15)
    nationality:str = Field(min_length=1, max_length=100)


class Race(BaseModel):
    raceId: int  = Field(gt=0, lt= 500000)
    raceYear: int = Field(gt=1925, lt= 2025)
    roundNumber: int = Field(gt=0, lt=100)
    circuitId: int = Field(gt=0, lt=500)
    raceName:str = Field(min_length=1, max_length=100)
    raceDate:str = Field(min_length=1, max_length=15)

class Result(BaseModel):
    resultId:int  = Field(gt=0, lt=50)
    raceId: int  = Field(gt=0, lt= 500000)
    driverId:int = Field(gt=0, lt= 500000)
    constructorId: int  = Field(gt=0, lt= 500000)
    resultNumber: str = Field(min_length=1, max_length=5)
    grid: int = Field(gt=0, lt=30)
    positionOrder: int = Field(gt=0, lt=30)
    points: float = Field(ge=10.000,le=10.000)
    laps: int = Field(gt=-1, lt=145)
    raceTime: str = Field(min_length=1, max_length=12)
    miliseconds: str = Field(min_length=1, max_length=12)
    fastestLap : str = Field(min_length=1, max_length=5)
    rankP: str = Field(min_length=1, max_length=5)
    fastestLapTime:str = Field(min_length=1, max_length=12)
    fastestLapSpeed: str = Field(min_length=1, max_length=12)
    statusId: int = Field(gt=0, lt= 300)




class Libro(BaseModel):
    titulo: str = Field(min_length=1)
    autor:str   = Field(min_length=1, max_length=100)
    descripcion: str = Field(min_length=1, max_length=250)
    rating: int = Field(gt=-1, lt=11) #Como el greater than, less than de assembler
    anio: int   = Field(gt=0, lt=2023)


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
