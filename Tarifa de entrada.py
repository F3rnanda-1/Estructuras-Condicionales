edad = int(input("Ingresa la edad de la persona: "))

if edad < 12:
    costo = 50
elif 12 <= edad <= 17:
    costo = 80
else: 
    costo = 120

print(f"La tarifa de entrada para una persona de {edad} años es: ${costo}")
