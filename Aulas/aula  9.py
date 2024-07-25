#laços de repedição for e while



llsta_nomes =["Felipe", "Mariana", "Ronaldo"];


for nome in llsta_nomes : 
    print(nome);


# range 


n = list (range(5));
print(n);

n = list(range(10,20));
print(n)

n = list (range(20,30,2));
print(n);

# -------------------------------

par =[]

impar=[]

for i in range(10,20):
    if  i % 2 == 0 :
        par.append(i)
    else:
        impar.append(i);

print ("Os números parea : ",par);
print( "Os números parea : ",impar);