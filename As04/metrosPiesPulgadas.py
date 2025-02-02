# Escribir un programa que lea un número que represente una distancia en metros y
# escriba su equivalente en pies y su equivalente en pulgadas. El resultado deberá
# desplegarse en notación de punto fijo con 4 cifras decimales. El archivo con el código
# fuente deberá llamarse metrosPiesPulgadas.py.

metros_pies = 3.28084
pies_pulgadas = 12.0

metros = float(input("Ingrese la distancia en metros: "))

pies = metros * metros_pies

pulgadas = pies * pies_pulgadas

print(f"{metros:.4f} metros son {pies:.4f} pies")
print(f"{metros:.4f} metros son {pulgadas:.4f} pulgadas")