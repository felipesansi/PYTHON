# Importação simples de um módulo padrão
import math

# Importação com alias de um módulo padrão
import datetime as dt

# Importação de funções específicas de um módulo padrão
from random import randint, choice

# Importação de um pacote externo (deve ser instalado via pip)
import requests

# Exemplo de função em um módulo personalizado (simulado aqui)
def saudacao(nome):
    """Simula um módulo personalizado com uma função de saudação."""
    return f"Olá, {nome}!"

# Função principal para demonstrar o uso das importações
def main():
    # Uso da importação simples
    numero = 9
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}")

    # Uso da importação com alias
    data_atual = dt.datetime.now()
    print(f"Data e hora atuais: {data_atual}")

    # Uso da importação de funções específicas
    numero_aleatorio = randint(1, 10)
    escolha_aleatoria = choice(['maçã', 'banana', 'laranja'])
    print(f"Número aleatório entre 1 e 10: {numero_aleatorio}")
    print(f"Escolha aleatória de fruta: {escolha_aleatoria}")

    # Uso de biblioteca externa
    try:
        resposta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        dados = resposta.json()
        print("\nDados obtidos da API:")
        print(f"Título: {dados['title']}")
        print(f"Corpo: {dados['body']}")
    except requests.exceptions.RequestException as e:
        print("Erro ao fazer requisição HTTP:", e)

    # Uso do módulo personalizado
    mensagem = saudacao("Maria")
    print("\nMensagem do módulo personalizado:")
    print(mensagem)

if __name__ == "__main__":
    main()
