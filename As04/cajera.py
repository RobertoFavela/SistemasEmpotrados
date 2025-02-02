# Escriba un programa que indique a una cajera de banco el número y denominación de
# los billetes que necesita darle a un cliente al hacer un retiro. La cajera deberá darle al
# cliente billetes de la más alta denominación posible, esto es, el menor número de billetes.
# Suponga que los retiros deben de ser en cantidades múltiples de 50 pesos y que hay
# billetes de $50, $100, $500 y $1000 pesos. El archivo con el código fuente deberá
# llamarse cajera.py.

def calcular_billetes(cantidad):
    if cantidad % 50 != 0:
        return "La cantidad debe ser múltiplo de 50"
    
    billetes = [1000, 500, 100, 50]
    resultado = {}
    
    for billete in billetes:
        if cantidad >= billete:
            num_billetes = cantidad // billete
            cantidad -= num_billetes * billete
            resultado[billete] = num_billetes
    
    return resultado

cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))

resultado = calcular_billetes(cantidad_retirar)
print(f"Para retirar {cantidad_retirar} pesos, la cajera debe entregar:")
for billete, cantidad in resultado.items():
    print(f"{cantidad} billetes de {billete} pesos")
