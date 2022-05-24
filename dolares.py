dolares = input("Cuantos dólares tienes?: ")
dolares = float(dolares)
pesos = 20
total = dolares * pesos
total = round(total, 2)
total = str(total)
print("Tienes $"+total+" pesos mexicanos en total")