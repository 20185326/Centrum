from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import smtplib
class ResponsableDeVenta:
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.leadsFaseNoCalificados = []
        self.leadsFasePocoPrometedora = []
        self.leadsFaseMedianamentePrometedora = []
        self.leadsFaseAltamentePrometedora = []
        self.leadsFaseUrgencia = []
    def imprimir_informacion(self):
      print("Informacion de la asesora",self.nombre)
      print("leadsFaseNoCalificados (notificacion)==============================")
      for lead in self.leadsFaseNoCalificados:
        lead.imprimir_detalles()
      print("leadsFasePocoPrometedora (notificacion)==============================")
      for lead in self.leadsFasePocoPrometedora:
        lead.imprimir_detalles()
      print("leadsFaseMedianamentePrometedora (notificacion)==============================")
      for lead in self.leadsFaseMedianamentePrometedora:
        lead.imprimir_detalles()
      print("leadsFaseAltamentePrometedora (notificacion)==============================")
      for lead in self.leadsFaseAltamentePrometedora:
        lead.imprimir_detalles()
      print("leadsFaseUrgencia (notificacion)==============================")
      for lead in self.leadsFaseUrgencia:
        lead.imprimir_detalles()
    def imprimir_informacion_correo(self):
        print("Informacion de la asesora", self.nombre)
        cadena = ""
        for indice, lead in enumerate(
                self.leadsFaseNoCalificados + self.leadsFasePocoPrometedora + self.leadsFaseMedianamentePrometedora +
                self.leadsFaseAltamentePrometedora + self.leadsFaseUrgencia, 1):
            cadena += f"<p style='font-size:14px;'>{lead.imprimir_notificacion(indice)}</p>"
        return cadena

class Lead:
    def __init__(self, id, nombre, dni, estado, sub_estado, fecha_creacion,
                 fecha_poco_prometedor, fecha_moderadamente_prometedor,
                 fecha_altamente_prometedor, responsable_id, responsable_nombre,
                 fecha_inaguracion_programa):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.estado = estado
        self.sub_estado = sub_estado
        self.fecha_creacion = fecha_creacion
        self.fecha_poco_prometedor = fecha_poco_prometedor
        self.fecha_moderadamente_prometedor = fecha_moderadamente_prometedor
        self.fecha_altamente_prometedor = fecha_altamente_prometedor
        self.responsable_id = responsable_id
        self.responsable_nombre = responsable_nombre
        self.fecha_inaguracion_programa=fecha_inaguracion_programa
        self.fase="Ninguna"
        self.dias=0
        self.ultima_fecha=None
        self.flag_correo=False
        self.flag_reasigna=False
        self.dias_faltantes_notificacion=0
        self.motivo_de_reasignacion=""

    def identificar_fase(self):
      if self.estado != "Dada de baja" and self.estado != "Convertida":
        hoy = datetime.today().strftime('%d/%m/%Y')
        if self.fecha_creacion!=None:
          self.fase="FaseNC"
          self.ultima_fecha=self.fecha_creacion
        if self.fecha_poco_prometedor!=None:
          self.fase="FasePP"
          self.ultima_fecha=self.fecha_poco_prometedor
        if self.fecha_moderadamente_prometedor!=None:
          self.fase="FaseMP"
          self.ultima_fecha=self.fecha_moderadamente_prometedor
        if self.fecha_altamente_prometedor!=None:
          self.fase="FaseAP"
          self.ultima_fecha=self.fecha_altamente_prometedor
        if self.diferencia_de_dias(hoy,self.fecha_inaguracion_programa)<=2:
          #En este caso la frecha pivote sera la ultima fecha , y la ultima fecha la fecha de inaguracion
          self.fase="FaseUD"


    def diferencia_de_dias(self, ultima_fecha,fecha_pivote):
      #Dias habiles
      self.dias = 0
      if isinstance(ultima_fecha, str):
          ultima_fecha = datetime.strptime(ultima_fecha, "%d/%m/%Y")
      if isinstance(fecha_pivote, str):
          fecha_pivote= datetime.strptime(fecha_pivote, "%d/%m/%Y")

      # Lista de días no laborables (puedes ajustarla según tus necesidades)
      dias_no_laborables = [5, 6]  # sábado y domingo

      while ultima_fecha <= fecha_pivote:
          # Si el día de la semana no está en la lista de días no laborables, incrementar los días hábiles
          if ultima_fecha.weekday() not in dias_no_laborables:
              self.dias += 1
          ultima_fecha += timedelta(days=1)
      if self.dias>0:
        self.dias-=1
      return self.dias



    def asignar_flag(self):
        hoy = datetime.today()
        if self.fase=="FaseNC":
          if self.diferencia_de_dias(self.ultima_fecha,hoy)>=1:
            self.flag_correo=True
            self.flag_reasigna=True
            self.dias_faltantes_notificacion=1
            self.motivo_de_reasignacion="Es un lead no convertido , a las 5pm de mañana se reasignara el lead si no se cambia de etapa"
        if self.fase=="FasePP":
          if self.diferencia_de_dias(self.ultima_fecha,hoy)>=14:
            self.flag_correo=True
            self.dias_faltantes_notificacion=3
            self.motivo_de_reasignacion="Es un lead poco prometedor, ya pasaron 14 dias o mas. En 3 dias a las 5pm reasignara el lead si no se cambia de etapa"
            if self.diferencia_de_dias(self.ultima_fecha,hoy)>=17:
              self.flag_reasigna=True
        if self.fase=="FaseMP":
          if self.diferencia_de_dias(self.ultima_fecha,hoy)>=8:
            self.motivo_de_reasignacion="Es un lead meadianamente prometedor, ya pasaron 8 dias o mas. En 2 dias a las 5pm reasignara el lead si no se cambia de etapa"
            self.dias_faltantes_notificacion=2
            self.flag_correo=True
            if self.diferencia_de_dias(self.ultima_fecha,hoy)>=10:
              self.flag_reasigna=True
        if self.fase=="FaseAP":
          #No se diagramo en el proceso pero se deja si es que se desea agregar
          pass
        if self.fase=="FaseUD":
          if self.diferencia_de_dias(hoy,self.fecha_inaguracion_programa)==2:
            self.flag_correo=True
            self.motivo_de_reasignacion="Si no se atiende este lead, el dia de mañana a las 5pm se reasignara el lead, debido a que el programa comienza en dos dias"
          if self.diferencia_de_dias(hoy,self.fecha_inaguracion_programa)==1:
            self.flag_reasigna=True
    def imprimir_detalles(self):
      print(f"ID: {self.id}")
      print(f"Nombre: {self.nombre}")
      print(f"DNI: {self.dni}")
      print(f"Estado: {self.estado}")
      print(f"Sub Estado: {self.sub_estado}")
      print(f"Fecha de Creación: {self.fecha_creacion}")
      print(f"Fecha Poco Prometedor: {self.fecha_poco_prometedor}")
      print(f"Fecha Moderadamente Prometedor: {self.fecha_moderadamente_prometedor}")
      print(f"Fecha Altamente Prometedor: {self.fecha_altamente_prometedor}")
      print(f"Responsable ID: {self.responsable_id}")
      print(f"Responsable Nombre: {self.responsable_nombre}")
      print(f"Fecha Inaguración Programa: {self.fecha_inaguracion_programa}")
      print(f"Fase: {self.fase}")
      print(f"Días: {self.dias}")
      print(f"Flag Correo: {self.flag_correo}")
      print(f"Flag Reasigna: {self.flag_reasigna}")
      print(f"Última Fecha: {self.ultima_fecha}")
    def imprimir_notificacion(self,indice):
      info_lead = (
          f"<p style='font-size:14px;'>"
          f"<b>Lead</b> numero {indice}<br>"
          f"<b>El lead con Nombre:</b> {self.nombre} <b>de DNI:</b> {self.dni}<br>"
          f"<b>En la Sub Estado:</b> {self.sub_estado}<br>"
          f"<b>Que fue atendido en Última Fecha:</b> {self.ultima_fecha}<br>"
          f"<b>Con programa de Fecha Inaguración Programa:</b> {self.fecha_inaguracion_programa}<br>"
          f"<b>Sera reasignado en:</b> {self.dias_faltantes_notificacion} días<br>"
          f"<b>Resumen:</b> {self.motivo_de_reasignacion}"
          f"</p>"
      )
      return info_lead


class GestorLeadsyRDV:
    def __init__(self):
        self.leads_CRM = []
        self.RDV_CRM = []
        self.remitente = "andre.zambrano.cueva@gmail.com"
        self.contraseña = "bfhf axya sijx fueb"
    #Obtener informacion del CRM o por FORM
    def obtener_leads_crm(self,leads_CRM):
        self.calcularCamposLeads(leads_CRM)
        self.leads_CRM=leads_CRM
    def obtener_rdvs_crm(self,RDV_CRM):
        self.RDV_CRM=RDV_CRM
    def obtener_leads_fuente_form(self):
      #Para implementaciones futuras
      pass

    #Si es que el lead existe en el CRM (camino 1)
    def buscar_rdvs(self, lead):
      #Flujo de reasignacion
      pass

    #Si es que el lead no existe en el CRM (camino 2)
    def lead_existe_en_crm(self, lead):
      #Para futuras impllementaciones (con api de oracle sales cloud)
      pass
    def crear_contacto(self, contacto):
      #Para futuras implementaciones (con api de oracle sales cloud)
      pass
    def crear_lead(self, lead):
      #Para futuras implementaciones (con api de oracle sales cloud)
      pass

    #Si  se creo el lead o ninguno de los RDVs que atendieron al lead cumple "X" condicion
    def aplica_ruleteo(self, boletos, responsable_venta):
      #Para futuras implementaciones (con api de oracle sales cloud)
      pass

    #Una ves que ya se sabe a 100% que asesor sera el que atienda al lead,
    #se reasigna(quita del rdv anterior y asigna al nuevo en su lista de leads )
    def reasignar_lead_al_rdv(self, lead, rdv):
      #Para futuras implementaciones (con api de oracle sales cloud)
      pass

    #Notificaciones


    def enviar_notificacion_por_correo(self):
        # Configurar los parámetros del servidor SMTP
        servidor_smtp = 'smtp.gmail.com'  # Para Gmail
        puerto_smtp = 587  # Puerto SMTP
        usuario_smtp = self.remitente
        contraseña_smtp = self.contraseña

        for rdv in self.RDV_CRM:
            # Crear el objeto mensaje
            msg = MIMEMultipart()
            msg['From'] = usuario_smtp
            msg['To'] = rdv.correo  # Cambiar por el correo del responsable de ventas
            msg['Subject'] = 'Notificación de RDV Previo'

            # Construir el cuerpo del mensaje con formato HTML
            mensaje = "<html><body>"
            mensaje += f"<p style='font-size:16px; font-weight:bold;'>Hola {rdv.nombre}, este es una notificacion de estado de tus leads.</p>"
            mensaje += "<p style='font-size:14px;'>Información de los leads que serán reasignados en los próximos días:</p>"

            # Obtener la información de los leads
            informacion_correo = self.imprimir_informacion_correo(rdv)
            mensaje += informacion_correo

            mensaje += "<p style='font-size:14px;'>Atentamente,</p>"
            mensaje += "<p style='font-size:14px;'>Sistema de Gestión de Leads y Responsables de venta</p>"
            mensaje += "</body></html>"

            msg.attach(MIMEText(mensaje, 'html'))

            # Iniciar conexión con el servidor SMTP y enviar el correo
            with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
                servidor.starttls()
                servidor.login(usuario_smtp, contraseña_smtp)
                servidor.send_message(msg)

            print("Correo de notificación enviado exitosamente.")

    # Esta función retorna la información del correo en lugar de imprimirlo
    def imprimir_informacion_correo(self, rdv):
      return rdv.imprimir_informacion_correo()

    def notificar_rdv_cambio(self, rdv):
        pass
    def buscarResponsableDeVentaActual(self, responsable_actual):
        for indice, responsable in enumerate(self.RDV_CRM):
            if responsable_actual == responsable.id:
                return indice
        return -1
    def asignar_lead_a_asesora_para_notificacion_previa(self):
        for lead in self.leads_CRM:
            encontrado = False
            for rdv in self.RDV_CRM:
                if lead.responsable_id == rdv.id:
                    encontrado = True
                    if lead.flag_correo and encontrado==True:
                        if lead.fase == "FaseNC":
                            rdv.leadsFaseNoCalificados.append(lead)
                        elif lead.fase == "FasePP":
                            rdv.leadsFasePocoPrometedora.append(lead)
                        elif lead.fase == "FaseMP":
                            rdv.leadsFaseMedianamentePrometedora.append(lead)
                        elif lead.fase == "FaseAP":
                            rdv.leadsFaseAltamentePrometedora.append(lead)
                        elif lead.fase == "FaseUD":
                            rdv.leadsFaseUrgencia.append(lead)
                        break
            if not encontrado:
                print("No se encontró un responsable correspondiente para el lead.")

    def calcularCamposLeads(self,leads):
        for lead in leads:
          lead.identificar_fase()
          lead.asignar_flag()
          #lead.imprimir_detalles()
          #print("\n======\n")
        return leads
    def imprimir_informacion_por_RDV(self):
      for rdv in self.RDV_CRM:
        rdv.imprimir_informacion()
        print("\n===================")
        