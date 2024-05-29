Pasos para que funcione correctamente:
A) El servidor de AWS esta configurado apra que solo pueda recibir solicitudes desde 
ciertas direcciones ip, de manera didactica puse solo mi IP personal de mi laptop
pero se debe agregar las direcciones ip de las involucradas, hasta que encontremos una 
forma mas eficiente (de ser el caso)

B) Se deben conectar a putty para prender el servidor en caso se apague, es recomendable
guardar la sesion para poder acceder facilmente.

C) Una ves la ip y el putty configurado correctamente, se debe prender servicio api.

Activar el app :
(previamente se configuro para que pueda recibir servicios api)-> en caso de usar otro servidor investigar: sudo nano /etc/nginx/nginx.conf
uvicorn main:app --host 0.0.0.0 --port 8000

Ver los servicios:
http://54.160.199.176:8000/docs

4- Servicio api listo para PUSH, GET, ETC
ver ejemplos en: FastApi-Centrum.ipynb


Pasos para que funcione correctamente:
A) Configuración del Servidor de AWS
El servidor de AWS está configurado para que solo pueda recibir solicitudes desde ciertas direcciones IP.
De manera didáctica, se ha configurado solo la IP personal de la laptop.
Se deben agregar las direcciones IP de todas las involucradas hasta encontrar una forma más eficiente (de ser el caso).
B) Conexión a Putty
Conéctate a Putty para encender el servidor en caso de que se apague.
Es recomendable guardar la sesión para poder acceder fácilmente.
C) Encender el Servicio API
Una vez la IP y Putty estén configurados correctamente, enciende el servicio API.

D)Activar la aplicación:
Previamente, se configuró para que pueda recibir servicios API.
En caso de usar otro servidor, investigar:
sudo nano /etc/nginx/nginx.conf
Ejecuta el siguiente comando para iniciar el servicio:
uvicorn main:app --host 0.0.0.0 --port 8000

E)Ver los Servicios
Accede a los servicios a través de la URL:
http://54.160.199.176:8000/docs

F)Servicio API Listo para PUSH, GET, ETC
Ver ejemplos en: FastApi-Centrum.ipynb