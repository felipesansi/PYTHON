# Tuplas

tuplas_num = [1,2,3.3,7,27,"python"]
tuplas_num.pop()
 
#acessos
print("Para acessar por posição ex: tuplas_num[0] ",tuplas_num[0])
print(tuplas_num[-1])
print(tuplas_num[:4])
print(tuplas_num[3:])
print(tuplas_num[2:6:2])
print("\n---------------\n")

#desenpacotamento
curso = ["python","Felipe", 10.00, 2024]
nc, na, nn, ano = curso;

print(nc)
print(nn)

# se quiser somente 1 ou mais elementos da tupla use o _,
nc, _, nn,_ = curso
print(nc);
print(nn);

tuplas_num = (1, 2, 3, 4)
print( "Tupla original :",tuplas_num)  

# Adicionando o elemento 5 à tupla
tuplas_num = tuplas_num + (5,)
print(tuplas_num)  

print(tuplas_num)  


tuplas_num = tuplas_num + (5,)
print("Tupla modificada: ",tuplas_num)  

# adicionando uma lista a tupla

minha_tupla =([1,2,3],[7,8.8,9],["python",-8])
print("minha tupla original: ", minha_tupla)
print("A Lista dentro da tupla na posição 0 : ",minha_tupla[0])
print("O elemento 0  da minha tupla é do tipo: ",type(minha_tupla[0]))

# adicionando a lista na pisição 0 da tupla
minha_tupla[0].append(5)
print(minha_tupla[0])