Pasos para que funcione correctamente:
1- El servidor de AWS esta configurado apra que solo pueda recibir solicitudes desde 
ciertas direcciones ip, de manera didactica puse solo mi IP personal de mi laptop
pero se debe agregar las direcciones ip de las involucradas, hasta que encontremos una 
forma mas eficiente (de ser el caso)

2- Se deben conectar a putty para prender el servidor en caso se apague, es recomendable
guardar la sesion para poder acceder facilmente.

3- Una ves la ip y el putty configurado correctamente, se debe prender servicio api.

Activar el app :
(previamente se configuro para que pueda recibir servicios api)-> en caso de usar otro servidor investigar: sudo nano /etc/nginx/nginx.conf
uvicorn main:app --host 0.0.0.0 --port 8000

Ver los servicios:
http://54.160.199.176:8000/docs

4- Servicio api listo para PUSH, GET, ETC
ver ejemplos en: FastApi-Centrum.ipynb
