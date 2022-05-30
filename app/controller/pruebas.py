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
preguntas=[]
# La siguiente consulta para obtener el set de preguntas entrenadas
query = "SELECT PREGUNTA FROM SET_PREGUNTAS"
cursor.execute(query)
contenido=cursor.fetchall()
preguntas=contenido
print(preguntas[0][0])
#df = pd.read_sql(query,cnxn)