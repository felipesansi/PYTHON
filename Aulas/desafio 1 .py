lista_pares = []

for n in range(1, 11):
    if n % 2 == 0:
        print(n)
        lista_pares.append(n**2)
        print(lista_pares)
