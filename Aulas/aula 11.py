# Definição da classe Carro
class Carro:
    def __init__(self):
        # O método __init__ é o construtor da classe, que é chamado quando uma nova instância da classe é criada.
        print("carro 1")  # Imprime "carro 1" quando uma instância da classe Carro é criada.

# Criando uma instância da classe Carro
Carro()

# Definição da classe Carro2
class Carro2:
    def __init__(self, ano, modelo, marca, statusFarol="Desligado"):
        # Inicializa a instância da classe Carro2 com os atributos ano, modelo, marca e status do farol.
        self.ano = ano  # Atributo para armazenar o ano do carro.
        self.modelo = modelo  # Atributo para armazenar o modelo do carro.
        self.marca = marca  # Atributo para armazenar a marca do carro.
        self.statusFarol = statusFarol  # Atributo para armazenar o estado do farol (Ligado/Desligado).
        self.velocimetro = 0  # Inicializa o velocímetro do carro com 0.
        self.__status = False  # Atributo privado para armazenar o status do carro.

    # Método para ligar o farol
    def LigarFarol(self):
        if self.statusFarol == "Desligado":
            # Verifica se o farol está desligado; se sim, liga o farol.
            self.statusFarol = "Ligado"
            print("Farol Ligado")
        else:
            # Se o farol já estiver ligado, informa o usuário.
            print("O farol já está ligado")

    # Método para desligar o farol
    def DesligarFarol(self):
        if self.statusFarol == "Ligado":
            # Verifica se o farol está ligado; se sim, desliga o farol.
            self.statusFarol = "Desligado"
            print("Farol Desligado")
        else:
            # Se o farol já estiver desligado, informa o usuário.
            print("O farol já está desligado")

    # Método para acelerar o carro
    def Acelerar(self, acrecimoVelocidade):
        # Aumenta a velocidade atual do carro pelo valor passado como parâmetro.
        self.velocimetro += acrecimoVelocidade
        print("Velocidade atual:", self.velocimetro)

    # Método para frear o carro
    def freiar(self, desacrecimoVelocidade=5):
        # Reduz a velocidade do carro pelo valor passado como parâmetro ou 5 por padrão.
        if self.velocimetro > desacrecimoVelocidade:
            self.velocimetro -= desacrecimoVelocidade
            print("Velocidade atual:", self.velocimetro)
        else:
            # Para o carro se a velocidade estiver abaixo do mínimo permitido para redução.
            self.velocimetro = 0
            print("Carro parado")

    # Método para obter o status (privado)
    def GetStatus(self):
        return self.__status
    
    # Método para definir o status (privado)
    def SetStatus(self, novo_status, chave):
        if chave == 26:
            self.__atualizar_status_motor(novo_status)
        else: 
            print("A chave não é a correta.")
    
    # Método privado para atualizar o status do motor
    def __atualizar_status_motor(self, novo_status):
        self.__status = novo_status
        print("Status do motor atualizado internamente para:", self.__status)

# Criando instâncias da classe Carro2 com diferentes atributos
gol = Carro2(2010, "gol", "wolks")
corola = Carro2(2018, "corolla", "toyota")
uno = Carro2(1990, "uno", "fiat", "Ligado")

# Imprime a velocidade inicial do carro Uno
print("Velocidade inicial do Uno:", uno.velocimetro)

# Acelera o carro Uno em 10 km/h
uno.Acelerar(10)

# Tenta ligar o farol do carro Uno (já está ligado por padrão)
uno.LigarFarol()

# Obtém o status privado do carro Uno
print("Status do Uno antes de alterar:", uno.GetStatus())

# Obtém a chave do usuário
chave_usuario = int(input("Digite a chave: "))

# Tenta alterar o status do carro Uno
uno.SetStatus(True, chave_usuario)

# Imprime o status atualizado do carro Uno
print("Status do Uno após tentativa de alteração:", uno.GetStatus())
