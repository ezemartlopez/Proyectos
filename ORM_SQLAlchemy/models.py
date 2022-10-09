import db
from sqlalchemy import Column, Integer, String, Float
class Producto(db.Base):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    total = Column(Float)
    cantidad = Column(Float)
    def __init__(self, nombre, total,cantidad):
        self.nombre = nombre
        self.total = total
        self.cantidad = cantidad
    def getId(self):
        return self.id
    def __repr__(self):
        return f'Producto({self.nombre}, {self.precio})'
    def __str__(self):
        return f'{self.nombre},cantidad:  {self.cantidad},  total: {self.total}'