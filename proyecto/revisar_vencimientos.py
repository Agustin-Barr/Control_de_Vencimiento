import json 
with open ('productos.json', 'r', encoding='utf-8') as vencimientos:
    productos = json.load(vencimientos)

print("productos cargados: ")
for producto in productos :
    print(f"- {producto['nombre']}|Vence : {producto['fecha_vencimiento']}| en {producto['sucursal']} ")