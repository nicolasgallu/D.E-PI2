from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, text


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(String, unique=True)
    email = Column(String, unique=True)
    contrasena = Column(String)

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    subcategorias = relationship("Subcategoria", back_populates="categoria")

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(String)
    precio = Column(Float)
    stock = Column(Integer)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))

#----------------------------------------------------------------------------------------------------

class Orden(Base):
    __tablename__ = 'ordenes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    fecha_orden = Column(DateTime)
    total = Column(Float)
    estado = Column(String)

class DetalleOrden(Base):
    __tablename__ = 'detalle_ordenes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    orden_id = Column(Integer)
    producto_id = Column(Integer)
    cantidad = Column(Integer)
    precio_unitario = Column(Float)

#----------------------------------------------------------------------------------------------------

class DireccionEnvio(Base):
    __tablename__ = 'direcciones_envio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    calle = Column(String)
    ciudad = Column(String)
    departamento = Column(String)
    provincia = Column(String)
    distrito = Column(String)
    estado = Column(String)
    codigo_postal = Column(String)
    pais = Column(String)

class Carrito(Base):
    __tablename__ = 'carrito'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    producto_id = Column(Integer, ForeignKey('productos.id'))
    cantidad = Column(Integer)
    fecha_agregado = Column(DateTime)

class MetodoPago(Base):
    __tablename__ = 'metodos_pago'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(String)

class OrdenMetodoPago(Base):
    __tablename__ = 'ordenes_metodopago'
    id = Column(Integer, primary_key=True, autoincrement=True)
    orden_id = Column(Integer)
    metodo_pago_id = Column(Integer)
    monto_pagado = Column(Float)

class HistorialPago(Base):
    __tablename__ = 'historial_pagos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    orden_id = Column(Integer)
    metodo_pago_id = Column(Integer)
    monto = Column(Float)
    fecha_pago = Column(DateTime)
    estado_pago = Column(String)


class ResenaProducto(Base):
    __tablename__ = 'resenas_productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer)
    producto_id = Column(Integer)
    calificacion = Column(Integer)
    comentario = Column(String)
    fecha = Column(DateTime)


#----------------------------------------------------------------------------------------------------

    
# Conexión a la base
engine = create_engine("postgresql+psycopg2://nicolas:5000@localhost:5432/test_db")

# Crear tablas
Base.metadata.create_all(engine)
print("Tablas creadas.")
