import pyodbc 

server='35.223.17.129'
bd='prueba'
userio='andradeleonid'
contrasenia='pO(>$zKJ~nG/Q5D~'

conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+bd+';UID='+userio+';PWD='+contrasenia+'')
print(conexion)


