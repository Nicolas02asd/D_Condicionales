
peso_kg = float(input("Ingrese peso en kilogramos: "))
altura_cm = float(input("Ingrese altura en centímetros: "))

altura_mts = (altura_cm/100)
imc = (peso_kg/(altura_mts**2))

# Filtro para números negativos o cero.
if imc <= 0:
    print("Ingrese datos validos")
else:
    print(f"Su IMC es {imc:.2f}")

    if imc<18.5:
        print("La clasificación OMS es Bajo Peso")
    elif 18.5<=imc<25:
        print("La clasificación OMS es Adecuado")
    elif 25<=imc<30:
        print("La clasificación OMS es Sobrepeso")
    elif 30<=imc<35:
        print("La clasificación OMS es Obesidad Grado I")
    elif 35<=imc<40:
        print("La clasificación OMS es Obesidad Grado II")
    elif imc>=40:
        print("La clasificación OMS es Obesidad Grado III")