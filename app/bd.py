import pyodbc 


def obtener_conexion():
    server='35.223.17.129'
    bd='prueba'
    userio='sqlserver'
    contrasenia='pO(>$zKJ~nG/Q5D~'

    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+bd+';UID='+userio+';PWD='+contrasenia+'')
    


