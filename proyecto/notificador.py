import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

##Para empezar cargo los datos del .env
load_dotenv()
#Cargando el .env , tomo las variables guardadas en el 
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
EMAIL_DESTINATARIO =  os.getenv('EMAIL_DESTINATARIO')
#funcion que envia un correo de alerta 
def enviar_alerta (mensaje, asunto='Alerta de vencimiento'):
    destino = EMAIL_DESTINATARIO
    msg = MIMEText(mensaje)
    msg['subject'] = asunto
    msg['FROM'] = EMAIL
    msg['to'] = destino
    
    try :
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
            server.login(EMAIL,PASSWORD)
            server.send_message(msg)
            print('Corre enviado')
    except Exception as e:
        print(f'Error al enviar correo : {e}')



