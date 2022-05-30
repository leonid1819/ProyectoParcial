# Importamos nuestro archivo bd.py
# Importamos pandas
from ctypes.wintypes import PINT
import sys  
sys.path.append("app")
from bd import obtener_conexion
import pandas as pd
import spacy
from math import sqrt

def squared_sum(x):
  """ return 3 rounded square rooted value """
  return round(sqrt(sum([a*a for a in x])),3)


def cos_similarity(x,y):
  """ return cosine similarity between two lists """
  numerator = sum(a*b for a,b in zip(x,y))
  denominator = squared_sum(x)*squared_sum(y)
  return round(numerator/float(denominator),3)


# De nuestro archivo bd.py llamamos la siguiente función
cnxn = obtener_conexion()
cursor = cnxn.cursor()

# La siguiente consulta para obtener el set de preguntas entrenadas
query = "SELECT [PREGUNTA],[RESPUESTA] FROM SET_PREGUNTAS"
df = pd.read_sql(query,cnxn)

preguntas = df['PREGUNTA'].to_list()
respuestas = df['RESPUESTA'].to_list()

pregunta_usuario = '¿Donde veo las vacantes?'
respuesta_usuario = ''

nlp = spacy.load("en_core_web_md")
indice = 0
similitudes = []

# Este ciclo for evalua todas las similitudes
for i in preguntas:
    try:
        contenedor = [nlp(i).vector,nlp(pregunta_usuario).vector]
        similitud = cos_similarity(contenedor[0],contenedor[1])
        similitudes.append(similitud)
    except:
        similitudes.append(0)

cnxn = obtener_conexion()
cursor = cnxn.cursor()
# Aca identificamos si la maxima similitud es mayor a 0.96
indice = similitudes.index(max(similitudes))
if max(similitudes) > 0.96:
    respuesta_usuario = respuestas[indice]
    cursor.execute("INSERT INTO TABLA_HECHOS (PREGUNTA,RESPUESTA) values(?,?)", pregunta_usuario,respuesta_usuario)
else:
    respuesta_usuario = "Disculpa, no puedo entenderte."
    cursor.execute("INSERT INTO SET_PREGUNTAS_FALLIDAS (PREGUNTA) values(?)", pregunta_usuario)

cnxn.commit()
cursor.close()