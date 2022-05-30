
import pyodbc 


def obtener_conexion():
    server='35.223.17.129'
    bd='prueba'
    userio='sqlserver'
    contrasenia='pO(>$zKJ~nG/Q5D~'

    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+bd+';UID='+userio+';PWD='+contrasenia+'')
"""
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


def obtener_conexion():
    server = '35.223.17.129' # to specify an alternate port
    database = 'prueba' 
    username = 'sqlserver' 
    password = 'pO(>$zKJ~nG/Q5D~'

    params = urllib.parse.quote_plus("'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password")

    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params,pool_pre_ping=True)


    return engine
"""