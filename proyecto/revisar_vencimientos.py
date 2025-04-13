import json 
from  datetime import datetime, timedelta
from notificador import enviar_alerta
# Comienzo a leer prodcutos.json y los agrego en una variable
with open ('productos.json', 'r', encoding='utf-8') as vencimientos:
    productos = json.load(vencimientos)


    
hoy = datetime.today()



#recorro la lista de productos y chequeo la fecha de vto comparandola con hoy
for producto in productos:#recolecto los datos de la variable productos
    nombre = producto['nombre']
    sucursal = producto['sucursal']
    fecha_str = producto['fecha_vencimiento']
    #convierto la fecha a un objeto de datetime(desde str a formato dias)
    fecha_venc = datetime.strptime(fecha_str,'%Y-%m-%d')
    dias_restante = (fecha_venc - hoy).days
    #chekeo si se cumple la fecha de vto o no 
    if dias_restante<= 15: 
        mensaje = f'ALERTA {nombre} | Vence en  {dias_restante}  | en {sucursal}'
        print(mensaje)
        enviar_alerta(mensaje)


    
