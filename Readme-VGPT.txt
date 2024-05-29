Configuración de Uvicorn como Servicio en una Instancia EC2

Paso 1: Conéctate a tu Instancia EC2
A) El servidor de AWS esta configurado apra que solo pueda recibir solicitudes desde 
ciertas direcciones ip, de manera didactica puse solo mi IP personal de mi laptop
pero se debe agregar las direcciones ip de las involucradas, hasta que encontremos una 
forma mas eficiente (de ser el caso)

B) Se deben conectar a putty para prender el servidor en caso se apague, es recomendable
guardar la sesion para poder acceder facilmente.

C) Una ves la ip y el putty configurado correctamente, se debe prender servicio api.

Paso 2: Instala Uvicorn y Dependencias
1. Actualiza el sistema e instala Python:
sudo yum update -y
sudo yum install python3 -y
2. Instala uvicorn y otras dependencias necesarias:
pip3 install uvicorn fastapi  # Ajusta según tus necesidades

Paso 3: Crear un Archivo de Servicio systemd
1. Crea y edita el archivo de servicio:
sudo nano /etc/systemd/system/uvicorn.service
2. Añade la siguiente configuración, ajustando las rutas y comandos según tu configuración:
[Unit]
Description=Uvicorn FastAPI app
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/Centrum  # Ajusta esto a tu ruta real
ExecStart=/usr/local/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
Environment="PATH=/usr/local/bin:/usr/bin:/bin"

[Install]
WantedBy=multi-user.target

Paso 4: Recargar systemd y Habilitar el Servicio
1. Recarga systemd:
sudo systemctl daemon-reload
2. Habilita el servicio para que se inicie automáticamente al arrancar el sistema:
sudo systemctl enable uvicorn.service
3. Inicia el servicio:
sudo systemctl start uvicorn.service

Paso 5: Verificar el Estado del Servicio
1. Revisa el estado del servicio para asegurarte de que se está ejecutando correctamente:
sudo systemctl status uvicorn.service

Paso 6: Configuración del Firewall
1. Ve a la consola de AWS EC2.
2. Selecciona tu instancia.
3. En la pestaña de "Security", encuentra y edita las reglas del grupo de seguridad asociado.
4. Añade una regla de entrada para permitir el tráfico en el puerto 8000.

Paso 7: Accede a tu Aplicación
Accede a tu aplicación Uvicorn a través de la dirección IP pública de tu instancia EC2 y el puerto 8000:
http://your-ec2-public-dns:8000

Nota
Para diagnosticar problemas, puedes revisar los registros del sistema:
journalctl -u uvicorn.service -b
