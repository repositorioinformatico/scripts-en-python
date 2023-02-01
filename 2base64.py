import base64 
import sys 
import os 
salir=False 
opcion=0 
def codifica32_64(tipo): 
  valorin=input("Inserta un texto para cifrar: ") 
  valor=str.encode(valorin) 
  if tipo == 32: 
   codificadoEnBase64=base64.b32encode(valor) 
  else: 
   codificadoEnBase64=base64.b64encode(valor) 
  print(codificadoEnBase64.decode("utf-8")) 
while not salir: 
os.system('clear') 
print("1. Opción 1") 
print("2. Opción 2") 
print("3. Salir") 
opcion=int(input("Elige una opción")) 
if opcion == 1: 
  print("Has seleccionado opción 1") 
  codifica32_64(32) 
  input("Pulse para continuar al menú") 
elif opcion == 2: 
  print("Has seleccionado opción 2") 
  codifica32_64(64) 
  input("Pulse para continuar al menú") 
elif opcion == 3: 
  exit(127) 
else: 
  input("Opción incorrecta.") 
