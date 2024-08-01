#função

def calcular(a, b, operacao="+"):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b

resultado1 = calcular(10, 5)  # Soma (valor padrão)
resultado2 = calcular(10, 5, operacao="-")  # Subtração
print(resultado1)  # Imprime 15
print(resultado2)  # Imprime 5

def exibir_dados(nome, idade, cidade="Desconhecida"):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

exibir_dados("João", 30)  # Imprime "Nome: João, Idade: 30, Cidade: Desconhecida"
exibir_dados("Maria", 25, cidade="São Paulo")  # Imprime "Nome: Maria, Idade: 25, Cidade: São Paulo"

# Função lambda que dobra o valor recebido
dobrar = lambda x: x * 2
print(dobrar(5))  # Imprime 10

# Convertendo temperaturas de Fahrenheit para Celsius usando lambda e list comprehension
fahrenheit_temps = [32, 50, 68, 86, 104]
celsius_temps = [(lambda f: (f - 32) * 5/9)(temp) for temp in fahrenheit_temps]
print(celsius_temps)  # Imprime [0.0, 10.0, 20.0, 30.0, 40.0]
 