menu = """
Bienvenido al conversor de monedas

1 - Pesos mexicanos
2.- Pesos colombianos
3.- Pesos argentinos

Elige una opción: 
"""
opcion = int(input(menu))

if opcion==1:
    pesos = input("Cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    dolar = 20
    total = pesos/dolar
    total = round(total, 2)
    total = str(total)
    print("Tienes $" + total + " dolares")
elif opcion == 2:
    pesos = input("Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    dolar = 4110
    total = pesos/dolar
    total = round(total, 2)
    total = str(total)
    print("Tienes $" + total + " dolares")
elif opcion == 3:
    pesos = input("Cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    dolar = 117
    total = pesos/dolar
    total = round(total, 2)
    total = str(total)
    print("Tienes $" + total + " dolares")
else: 
    print("Escoge una opción que esté aquí")



