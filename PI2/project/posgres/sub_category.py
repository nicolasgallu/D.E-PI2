from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


#Connection
engine = create_engine("postgresql+psycopg2://nicolas:5000@localhost:5432/test_db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    subcategorias = relationship("Subcategoria", back_populates="categoria")


#New Sub-Categories.
class Subcategoria(Base):
    __tablename__ = "subcategorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="subcategorias")


subcategorias_por_categoria = {
    "Electrónica": [
        "Teléfonos inteligentes",
        "Computadoras",
        "Accesorios electrónicos",
        "Dispositivos inteligentes"
    ],
    "Moda": [
        "Ropa para hombres",
        "Ropa para mujeres",
        "Calzado",
        "Bolsos",
        "Accesorios de moda"
    ],
    "Hogar y Cocina": [
        "Muebles",
        "Electrodomésticos",
        "Utensilios de cocina",
        "Decoración para el hogar"
    ],
    "Deportes y Aire Libre": [
        "Equipamiento deportivo",
        "Ropa deportiva",
        "Artículos para aire libre"
    ],
    "Belleza y Cuidado Personal": [
        "Cosméticos",
        "Productos para el cabello",
        "Productos para la piel",
        "Aseo personal"
    ],
    "Juguetes y Juegos": [
        "Juguetes para todas las edades",
        "Juegos de mesa",
        "Juguetes didácticos",
        "Juguetes electrónicos"
    ],
    "Automotriz": [
        "Accesorios para vehículos",
        "Repuestos para vehículos"
    ],
    "Libros y Papelería": [
        "Libros",
        "Cuadernos",
        "Útiles escolares",
        "Útiles de oficina"
    ],
    "Salud": [
        "Vitaminas",
        "Suplementos",
        "Productos médicos"
    ],
    "Mascotas": [
        "Alimentos para mascotas",
        "Juguetes para mascotas",
        "Productos para el cuidado de mascotas"
    ],
    "Tecnología y Gadgets": [
        "Innovaciones tecnológicas",
        "Productos novedosos"
    ],
    "Videojuegos": [
        "Consolas",
        "Juegos físicos y digitales",
        "Accesorios gamer"
    ]
}



#Creat table in base.
Base.metadata.create_all(engine)

#Extract and save sub-categories.
for nombre_cat, subcats in subcategorias_por_categoria.items():
    categoria = session.query(Categoria).filter_by(nombre=nombre_cat).first()
    if categoria:
        for sub_nombre in subcats:
            sub = Subcategoria(nombre=sub_nombre, categoria=categoria)
            session.add(sub)

session.commit()
session.close()
print("Subcategorías extraídas y cargadas con éxito.")
