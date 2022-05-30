# Importamos nuestro archivo bd.py
# Importamos pandas
import sys  
sys.path.append("app")
from bd import obtener_conexion
import pandas as pd

# De nuestro archivo bd.py llamamos la siguiente función
cnxn = obtener_conexion()
cursor = cnxn.cursor()

# La siguiente consulta para obtener el set de preguntas entrenadas
query = "SELECT [PREGUNTA],[RESPUESTA] FROM SET_PREGUNTAS"
df = pd.read_sql(query,cnxn)

print(df)