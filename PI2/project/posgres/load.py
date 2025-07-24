import pandas as pd
from sqlalchemy import create_engine

# Conexión a la base
engine = create_engine("postgresql+psycopg2://nicolas:5000@localhost:5432/test_db")

# Ruta base
ruta = "/home/nicolas/Escritorio/Bootcamp D.E/PI2/project/data/CSV/"

# Cargar usuarios
usuarios_df = pd.read_csv(ruta + "usuarios.csv")
usuarios_df.columns = ["nombre", "apellido", "dni", "email", "contrasena"]
usuarios_df.to_sql("usuarios", engine, if_exists="append", index=False)

# Cargar categorías
categorias_df = pd.read_csv(ruta + "categorias.csv")
categorias_df.columns = ["nombre", "descripcion"]
categorias_df.to_sql("categorias", engine, if_exists="append", index=False)

# Cargar productos
productos_df = pd.read_csv(ruta + "productos.csv")
productos_df.columns = ["nombre", "descripcion", "precio", "stock", "categoria_id"]
productos_df.to_sql("productos", engine, if_exists="append", index=False)

#----------------------------------------------------------------------------------------------------

# Cargar ordenes
ordenes_df = pd.read_csv(ruta + "ordenes.csv")
ordenes_df.columns = ["usuario_id", "fecha_orden", "total", "estado"]
ordenes_df.to_sql("ordenes", engine, if_exists="append", index=False)

# Cargar detalle_ordenes
detalle_df = pd.read_csv(ruta + "detalle_ordenes.csv")
detalle_df.columns = ["orden_id", "producto_id", "cantidad", "precio_unitario"]
detalle_df.to_sql("detalle_ordenes", engine, if_exists="append", index=False)


#----------------------------------------------------------------------------------------------------

# Direcciones de envío
direcciones_df = pd.read_csv(ruta + "direcciones_envio.csv")
direcciones_df.columns = ["usuario_id", "calle", "ciudad", "departamento", "provincia", "distrito", "estado", "codigo_postal", "pais"]
direcciones_df.to_sql("direcciones_envio", engine, if_exists="append", index=False)

# Carrito
carrito_df = pd.read_csv(ruta + "carrito.csv")
carrito_df.columns = ["usuario_id", "producto_id", "cantidad", "fecha_agregado"]
carrito_df.to_sql("carrito", engine, if_exists="append", index=False)

# Métodos de pago
metodos_pago_df = pd.read_csv(ruta + "metodos_pago.csv")
metodos_pago_df.columns = ["nombre", "descripcion"]
metodos_pago_df.to_sql("metodos_pago", engine, if_exists="append", index=False)

# Ordenes - método de pago
orden_mp_df = pd.read_csv(ruta + "ordenes_metodospago.csv")
orden_mp_df.columns = ["orden_id", "metodo_pago_id", "monto_pagado"]
orden_mp_df.to_sql("ordenes_metodopago", engine, if_exists="append", index=False)

# Reseñas productos
resenas_df = pd.read_csv(ruta + "resenas_productos.csv")
resenas_df.columns = ["usuario_id", "producto_id", "calificacion", "comentario", "fecha"]
resenas_df.to_sql("resenas_productos", engine, if_exists="append", index=False)

# Historial pagos
historial_df = pd.read_csv(ruta + "historial_pagos.csv")
historial_df.columns = ["orden_id", "metodo_pago_id", "monto", "fecha_pago", "estado_pago"]
historial_df.to_sql("historial_pagos", engine, if_exists="append", index=False)


print("Datos cargados correctamente.")
