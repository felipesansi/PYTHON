#parse do python

n_intero = input("Digite um númro inteiro: ");

# para converter um número para float. float(variavel com numero inteiro)
n_real= float(n_intero);

# mostrar número convartido 
print("O número: ", n_real);

print("\n---------//----------\n\n")

#----------------------------------------------------


n_float = input("\nDigite um número float: ");

# para converter um número para int. int(float(variável do número float))
n_2 = int(float(n_float));

# mostrar número convartido 
print("\nO número: ", n_2);

n3 =  input("\nDigite um númro: ");
# para converter um número para string.   str(variavel com numero)
numero_string = str(n3);

print("\n O número: ", numero_string ," se converteu para string\n" )

#verificar o tipo das variaveis type(variavel)
print("\nO valor da variável n_inteiro: ",n_intero, "esta variável é tipo: ",type(n_intero),"\n" );

# para contar numero de caracteres len(variável)
m = input("\nDigite um e-mail: ");
contagem = len(m);

# mostrar contagem de caracteres
print("\nO seu e-mail ",m," contém:", contagem);

n_3 = 27.45678;

# para pegar um numero especifico depois da vírgula round(variavel, numero de casas que você deseja)
print("\n\nO valor: ", n_3, "arredondado fica:  ", round(n_3,2));