calificacion = float(input("Ingresa tu calificación (0-100): "))

if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion < 90:
    letra = "B"
elif 70 <= calificacion < 80:
    letra = "C"
elif 60 <= calificacion < 70:
    letra = "D"
elif 0 <= calificacion < 60:
    letra = "F"
else:
    letra = None  

if letra:
    print(f"Tu calificación es {calificacion}, equivalente a {letra}.")
else:
    print("La calificación ingresada no es válida. Debe estar entre 0 y 100.")
