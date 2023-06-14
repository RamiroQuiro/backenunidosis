def pacienteEntity(item) ->dict:
    return {
        "episodio":item[0],
        "numSecuencia":item[1],
        "idMedicamento":item[2],
        "medicamento":item[3],
        "cantidad":item[4],
        "unidad":item[5],
        "frecuenciaHoras":item[6],
        "edadd":item[6],
        "indicaciones":item[7],
        "paciente":item[8],
        "nombrePaciente":item[9],
        "edad1":item[10],
        "servicio":item[12],
    }
    
def pacientesEntity(entity) -> list:
    [pacienteEntity(item) for item in entity]