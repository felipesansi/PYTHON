# operadores
n1 = float(input("\nDigite um número: "));
n2 = float (input("\nDigite um segundo número: "));

sub =  n1 - n2;
soma = n1 + n2;
div = n1 / n2; 
multi = n1 * n2;
pot = n1 ** n2; 
rest = n1 % n2;
div_int = n1//n2;
print("\n\n-----------------------------\n\n");
print("\nsoma = ", soma);
print("\nsubtração = " , sub);
print("\ndivisão = ", div);
print("\nmultiplicação = ", multi)
print("\npontência = ", pot);
print("\nresto = ", rest);
print("\nDivisão inteira = ", div_int);

print("\n\n-----------------------------\n\n");

print("usando funçao do python para ter o resto e a div ", divmod(n1,n2));

print("usando funçao do python para ter a pontência  ", pow(n1,n2));

# operadores logicos and, or, not
a = True;
b = False;
a and b;
a or b;
not a 

# operadores relacionais

a = 3;
b = 4;

c = a < b;
d = a > b;
e = a == b;
print(c);
print(d);
print(e);


print("A variável a è menor que 3? ", a < 3);

print("A variável a è menor igual que 3? ", a <= 3);

print("A variável b está entre [1, 3]?", 1 <= b <=3);

x=10;
y =5;
z = 10;

print("x == y ?", x == y);
print("x == z ?", x == z);
print("x != z ?", x != y);