import pyodbc
from schemas.paciente import pacienteEntity,pacientesEntity

connection=pyodbc.connect('DRIVER={SQL Server};SERVER={ip};DATABASE={name};UID=usiario;PWD=password')
# try:
#     # connection=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=172.16.3.94;DATABASE=registrobilletes;UID=ramiro;PWD=quirogon')
#     print('conexion exitosa')
#     cursor = connection.cursor()
#     cursor.execute("exec MedicamentosPorSala @Servicio='UTI'")
#     rows=cursor.fetchall()
#     for row in rows:
#         row_to_list = [elem for elem in row]
#         schema=pacienteEntity(row_to_list)
#         print(schema)
# except Exception as ex:
#     print(ex)
# finally:
#     connection.close()
#     print('coneccion finalizada')

