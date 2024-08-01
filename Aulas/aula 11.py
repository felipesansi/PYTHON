# Definição da classe Carro
class Carro():
    def __init__(self):
        print("carro 1")
        pass

# Criando uma instância da classe Carro
Carro()

# -------------------------

# Definição da classe Carro2
class Carro2():
    def __init__(self, ano, modelo, marca):
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        print(marca)
        print(modelo)
        print(ano)

# Criando uma instância da classe Carro2 com valores específicos
Carro2("GLE", "2020", "Toyota")  # Imprime "Toyota", "2020" e "GLE"
