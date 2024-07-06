#manipulando string

curso =  "fundamentos esseciais para python";

print("\n", curso)

#pegando letra como vetor
print( "\nPrimeira letra da variável curso ex = curso[0] : ", curso[0]);

#vetor de tras para frente
print("\nPrimeira letra de trás para frente da variável curso ex = curso[-1] : ",curso[-1]);

# se colocar : dentro do vetor pega do inicio até a posição que você inicar 
print("\ncolocar : dentro do vetor pega do inicio até a posição que você inicar ex = curso[ :11]  : ",curso[:11]);

# faz a mesma coisa só que de tras para frente
print("\nFaz a mesma coisa só que de tras para frente ex = curso[-5: ] : ",curso[-5:]);

#misto
print("\nAcesso misto começando na posição 6 indo até -9 ex = curso[6:-9] : ",curso[6:-9]);

#negativo
print("\nNegativo também pode acessar, somente comece por um número maior para menor ex =curso[-10:-3] : ",curso[-10:-3]);

# acessar por step,  da 0 pisicao ate a 12 pulando 3 em 3
print("\nAcessar por step,  da 0 pisicao ate a 12 pulando 3 em 3 ex = curso[0:12:3] : ",curso[0:12:3]);

#O exemplo a seguir é  do incio até o fim pulando uma letra e mostrando a sequinte
print("\nO exemplo a seguir é  do incio até o fim pulando uma letra e mostrando a sequinte ex = curso[ : :-1]",curso[::-1]);

print("\n\n ")
#concatenando string

nome  = "Felipe";
idade = 27;

print("\nO "+ nome + " tem " +str(idade) +" anos");

# repitindo  string 
print("\nO Nome repetido fica: "+ 3* nome);
print("\nO NOME : "+ nome + "CONTÊM A LETRA U :" , "U" in nome);

#------------------------------

# metodo em string

linguagem = "PYTHON";

print("\nPara saber quantos A tem na variável curso ex =  curso.count('a') :", curso.count('a'));

print("\nPara saber em qual posição está uma letra ou frase da string  ex = curso.find('para') :", curso.find("para"));
print("\nreplace é igual C#, substitui uma palavra por outra :  ", curso.replace("python", "c#"));
print("\nupper tranforma toda string em maiuscúla: ",curso.upper());
print("\nlower tranforma toda string em minuscúla: ", linguagem.lower());
print("\nO metodo capitalze deixa a primera letra da string maiuscúla: ",curso.capitalize());
print("\nO metodo split tranforma cada palavra em uma lista ", curso.split());
print("\nO metodo split tranforma cada palavra em uma lista, mas também pode passar aonde ele corta  : ", curso.split('s'));
splipt1 = curso.split();
splipt2 = curso.split('s');
print("\nO metoodo join faz isso: ", '-'.join(splipt1));
print("\nO metodo startswith erifica se a string texto começa com a palavra:", curso.startswith("7"))
print("\nO metoodo join faz isso: ", 'S'.join(splipt2));
nova_frase = "       Felipe é um programador       ";

print("\nO metodo strip tira todos os espaços extras da frase:", nova_frase.strip());

print("\nO metodo strip tira todos os espaços extras do começo da frase:", nova_frase.lstrip());

print("\nO metodo strip tira todos os espaços extras do final da frase:", nova_frase.rstrip());


#format
setor = "RH"
frase_format = "\n{} está no departamento de {}".format(nome, setor)
print(frase_format);

