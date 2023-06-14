from fastapi import APIRouter
from config.conexion_sqlserver import connection
from schemas.paciente import pacienteEntity,pacientesEntity

user=APIRouter()


@user.get('/user/{servicio}')
def get_user(servicio:str):
    try:
        print('conexion exitosa')
        cursor = connection.cursor()
        cursor.execute("exec MedicamentosPorSala @Servicio='"+servicio+"'")
        rows=cursor.fetchall()
        myArray=[]
        for row in rows:
            row_to_list = [elem for elem in row]
            schema=pacienteEntity(row_to_list)
            myArray.append(schema)
        return {servicio:myArray}
    except Exception as ex:
        print(ex)
    # finally:
    #     connection.close()
    #     print('coneccion finalizada')
