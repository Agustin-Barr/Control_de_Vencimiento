import json 
with open ('productos.json', 'r', encoding='utf-8') as vencimientos:
    productos = json.load(vencimientos)

print("productos cargados: ")
for producto in productos :
