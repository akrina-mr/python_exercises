number = int(input("Write a number:"))

# Si es:
# - mayor que 100 → imprimir "Grande"
# - entre 50 y 100 → imprimir "Mediano"
# - menor que 50 → imprimir "Pequeño"

if number < 50:
    print("Pequeño")
elif number <= 100:
    print("Mediano")
else:
    print("Grande")

