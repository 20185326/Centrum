from datetime import datetime, timedelta
from clases import GestorLeadsyRDV, ResponsableDeVenta, Lead

def obtenerLeads():
    fecha_hoy = datetime.now()
    # Fase 1
    lead1 = Lead(id=1, nombre="Juan Pérez", dni="12345678", estado="No Calificada", sub_estado="No Calificada", fecha_creacion=fecha_hoy - timedelta(hours=1), fecha_poco_prometedor=None, fecha_moderadamente_prometedor=None, fecha_altamente_prometedor=None, fecha_inaguracion_programa="10/10/2025", responsable_id=12345, responsable_nombre="RDV1")
    lead2 = Lead(id=2, nombre="María Gómez", dni="23456789", estado="No Calificada", sub_estado="No Calificada", fecha_creacion=fecha_hoy - timedelta(days=3,hours=1), fecha_poco_prometedor=None, fecha_moderadamente_prometedor=None, fecha_altamente_prometedor=None, fecha_inaguracion_programa="10/01/2025", responsable_id=12346, responsable_nombre="RDV2")
    # Fase 2
    lead3 = Lead(id=3, nombre="Carlos López", dni="34567890", estado="Calificada", sub_estado="Poco Prometedora", fecha_creacion="03/01/2024", fecha_poco_prometedor= fecha_hoy - timedelta(days=17,hours=1), fecha_moderadamente_prometedor=None, fecha_altamente_prometedor=None, fecha_inaguracion_programa="10/01/2025", responsable_id=12346, responsable_nombre="RDV2")
    lead4 = Lead(id=4, nombre="Ana Fernández", dni="45678901", estado="Calificada", sub_estado="Poco Prometedora", fecha_creacion="04/01/2024", fecha_poco_prometedor=fecha_hoy - timedelta(days=19,hours=1), fecha_moderadamente_prometedor=None, fecha_altamente_prometedor=None, fecha_inaguracion_programa="10/01/2025", responsable_id=12345, responsable_nombre="RDV1")
    # Fase 3
    lead5 = Lead(id=5, nombre="Luis Martínez", dni="56789012", estado="Calificada", sub_estado="Medianamente Prometedora", fecha_creacion="05/01/2024", fecha_poco_prometedor="14/01/2024", fecha_moderadamente_prometedor=fecha_hoy - timedelta(days=11,hours=1), fecha_altamente_prometedor=None, fecha_inaguracion_programa="10/01/2025", responsable_id=12345, responsable_nombre="RDV1")
    lead6 = Lead(id=6, nombre="Laura Sánchez", dni="67890123", estado="Calificada", sub_estado="Medianamente Prometedora", fecha_creacion="06/01/2024", fecha_poco_prometedor="15/01/2024", fecha_moderadamente_prometedor=fecha_hoy - timedelta(days=13,hours=1), fecha_altamente_prometedor=None, fecha_inaguracion_programa="10/01/2025", responsable_id=12346, responsable_nombre="RDV2")
    lead7 = Lead(id=7, nombre="Jorge Ramírez", dni="78901234", estado="Calificada", sub_estado="Medianamente Prometedora", fecha_creacion="07/01/2024", fecha_poco_prometedor="16/01/2024", fecha_moderadamente_prometedor="26/01/2024", fecha_altamente_prometedor=None, fecha_inaguracion_programa=fecha_hoy - timedelta(days=3,hours=1), responsable_id=12346, responsable_nombre="RDV2")
    #FASE X
    lead8 = Lead(id=8, nombre="Isabel Torres", dni="89012345", estado="No Calificada", sub_estado="No Calificada", fecha_creacion="08/01/2024", fecha_poco_prometedor=None, fecha_moderadamente_prometedor=None, fecha_altamente_prometedor=None, fecha_inaguracion_programa=fecha_hoy + timedelta(days=3,hours=1), responsable_id=12346, responsable_nombre="RDV2")
    lead9 = Lead(id=9, nombre="Ricardo Ortiz", dni="90123456", estado="Calificada", sub_estado="Medianamente Prometedora", fecha_creacion="09/01/2024", fecha_poco_prometedor="18/01/2024", fecha_moderadamente_prometedor="18/01/2024", fecha_altamente_prometedor="07/02/2024", fecha_inaguracion_programa=fecha_hoy + timedelta(days=4,hours=1), responsable_id=12346, responsable_nombre="RDV2")
    lead10 = Lead(id=10, nombre="Elena Vargas", dni="01234567", estado="Dada de baja", sub_estado="Dada de baja", fecha_creacion="10/01/2024", fecha_poco_prometedor="19/01/2024", fecha_moderadamente_prometedor="16/01/2024", fecha_altamente_prometedor="08/02/2024", fecha_inaguracion_programa=fecha_hoy + timedelta(days=4,hours=1), responsable_id=12345, responsable_nombre="RDV1")
    lead11 = Lead(id=11, nombre="Lead11", dni="0123456711", estado="Convertida", sub_estado="Convertida", fecha_creacion="10/01/2024", fecha_poco_prometedor="19/01/2024", fecha_moderadamente_prometedor="16/01/2024", fecha_altamente_prometedor="08/02/2024", fecha_inaguracion_programa=fecha_hoy + timedelta(days=4,hours=1), responsable_id=12346, responsable_nombre="RDV2")
    # Lista de todos los leads creados
    return [lead1, lead2, lead3, lead4, lead5, lead6, lead7, lead8, lead9, lead10, lead11]
def obtenerResponsables():
    responsable1 = ResponsableDeVenta(id=12345, nombre="RDV1", correo="andre.zambrano@pucp.edu.pe")
    responsable2 = ResponsableDeVenta(id=12346, nombre="RVD2", correo="andre.zambrano.cueva@gmail.com")
    return  [responsable1,responsable2]

