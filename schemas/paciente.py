def pacienteEntity(item) ->dict:
    return {
        "Episodio":item[0],
        "Num_Secuencia":item[1],
        "ID_Medicamento":item[2],
        "Medicamento":item[3],
        "Cantidad":item[4],
        "Unidad":item[5],
        "Frecuencia_Horas":item[6],
        "Indicaciones":item[6],
        "ID_Paciente":item[7],
        "Paciente":item[8],
        "Edad":item[9],
        "Edad1":item[10],
        "servicio":item[12],
    }
    
def pacientesEntity(entity) -> list:
    [pacienteEntity(item) for item in entity]