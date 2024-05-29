import uvicorn
from fastapi import FastAPI
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from clases import GestorLeadsyRDV
from InicializaPrueba import obtenerLeads, obtenerResponsables

#APP
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/enviar-correos-previo/")
def enviar_correos():
    #Datos de prueba
    responsables=obtenerResponsables()
    leads=obtenerLeads()
    #Gestor asumiendo que ya se obtudo la informacion anterior a travez de API de los rdv y de los leads
    gestor=GestorLeadsyRDV()
    gestor.obtener_leads_crm(leads)
    gestor.obtener_rdvs_crm(responsables)
    gestor.asignar_lead_a_asesora_para_notificacion_previa()
    #gestor.imprimir_informacion_por_RDV()
    gestor.enviar_notificacion_por_correo()
    return {"message": "Tarea de envío de correos encolada"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)