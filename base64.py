#codificar en base64
import base64
valorin=input("Inserta un texto para cifrar: ")
valor=str.encode(valorin)
codificadoEnBase64=base64.b64encode(valor)
print(codificadoEnBase64.decode("utf-8"))
