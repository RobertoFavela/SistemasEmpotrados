# Escribir un programa que lea un número que represente el radio de una esfera y escriba
# su área y volumen. El resultado deberá desplegarse en notación flotante con 6 cifras
# decimales. El archivo con el código fuente deberá llamarse areaVolumenEsfera.py.

import math

radio = float(input("Ingrese el radio de la esfera: "))

area = 4 * math.pi * radio ** 2
volumen = (4/3) * math.pi * radio ** 3

print(f"Área: {area:.6f}")
print(f"Volumen: {volumen:.6f}")