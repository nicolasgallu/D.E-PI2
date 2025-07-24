import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

# Conexión (ajustá según tu config)
engine = create_engine("postgresql+psycopg2://nicolas:5000@localhost:5432/test_db")
Session = sessionmaker(bind=engine)
session = Session()


# Lista de nombres de tablas
tablas = [
    "usuarios", 
    "carrito",
    "detalle_ordenes",
    "direcciones_envio",
    "historial_pagos",
    "metodos_pago",
    "ordenes",
    "ordenes_metodopago",
    "productos",
    "resenas_productos",
    "subcategorias"
]

def cargar_tabla(nombre_tabla):
    query = text(f"SELECT * FROM {nombre_tabla};")
    return pd.read_sql(query, engine)

def analizar_nulos_y_guardar(tablas, archivo_salida="reporte_nulos.txt"):
    with open(archivo_salida, "w", encoding="utf-8") as f:
        for tabla in tablas:
            df = cargar_tabla(tabla)
            nulos = df.isnull().sum()
            
            f.write(f"--- Tabla: {tabla} ---\n")
            f.write(f"Total filas: {len(df)}\n")
            f.write("Nulos por columna:\n")
            
            for col, cant_nulos in nulos.items():
                f.write(f"  {col}: {cant_nulos}\n")
            f.write("\n")
    print(f"Reporte de valores nulos guardado en '{archivo_salida}'.")




def detectar_duplicados_usuarios(archivo_salida="duplicados_usuarios.txt"):
    usuarios_df = cargar_tabla("usuarios")
    
    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write(f"Total filas en usuarios: {len(usuarios_df)}\n\n")
        
        # Duplicados por DNI
        duplicados_dni = usuarios_df[usuarios_df.duplicated(subset=['dni'], keep=False)]
        f.write(f"Duplicados por DNI ({len(duplicados_dni)} filas):\n")
        if len(duplicados_dni) > 0:
            f.write(duplicados_dni.to_string(index=False))
        else:
            f.write("No se encontraron duplicados por DNI.\n")
        f.write("\n\n")
        
        # Duplicados por Email
        duplicados_email = usuarios_df[usuarios_df.duplicated(subset=['email'], keep=False)]
        f.write(f"Duplicados por Email ({len(duplicados_email)} filas):\n")
        if len(duplicados_email) > 0:
            f.write(duplicados_email.to_string(index=False))
        else:
            f.write("No se encontraron duplicados por Email.\n")
        f.write("\n")
    
    print(f"Reporte de duplicados en usuarios guardado en '{archivo_salida}'.")


# Ejecutar el análisis
analizar_nulos_y_guardar(tablas)

# Ejecutar la función
detectar_duplicados_usuarios()
