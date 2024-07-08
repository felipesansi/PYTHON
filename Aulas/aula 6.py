# Estrutura de dados

lista_cursos = ["ADM", "ADS", "FISIO", "DIRETO", "MARKETING"];
lista_notas = [10, 7.5, 5.8, 4];

print("\nA manipulação de lista é parecida com manipulação de string")
print("\nPara acessar o primeiro e ultimo número da lista basta usar lista[0] e lista[-1] EX: ", lista_cursos[0], "," , lista_cursos[-1]);

print("\nAcessar todos elementos da lista até uma posição especifica é lista[:3] Ex: ",lista_notas[:3])

nova_lista = lista_cursos[::2] 

print("\npara manipular a lista para pular um elemento a cada elemento mostrado até o final da lista use ista_cursos[::2] ex",nova_lista)

lista_mista = lista_cursos + lista_notas

print("\nconcatenar elemento na lista use o +", lista_mista)

print("\npara repetir a lista use o * ", lista_notas*2);
print (lista_notas);

print("\npara remover elemento da lista use o metodo remove", lista_cursos.remove('ADS'));
print(lista_cursos);

print("\npara adicionar elemento da lista use o metodo append", lista_cursos.append('educação fisica'));
print(lista_cursos);


print("\npara remover o ultimo elemento da lista use o metodo pop sem parâmentro", lista_cursos.pop());
print(lista_cursos);


print("\npara remover elemento pelo indice da lista use o metodo pop(2) ", lista_cursos.pop(2));
print(lista_cursos);


print("\npara ordenar lista alfabeticamene use o metodo sort ", lista_cursos.sort());
print(lista_cursos);


print("\npara ordenar lista alfabeticamene use o metodo sort ", lista_notas.sort());
print(lista_notas);

