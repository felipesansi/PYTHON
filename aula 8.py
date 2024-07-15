# dicionarios

dicionarioSetores = {"Comercial":"ana", "Financeiro":"João", "adm":"Gabi", "Tecnologia":"Felipe"}
dicionario2 ={"a":3.65, 8:"yellow"}
print(dicionarioSetores)
print(dicionarioSetores["Tecnologia"])
print("Quantos elementos tem no dicionarioSetores: ",len(dicionarioSetores));
print("tem a chave Tecnologia em  dicionarioSetores: "  , "Tecnologia" in dicionarioSetores)
print("Executivo"not in dicionarioSetores)
dicionarioSetores ["Executivo"]= "Rafael"
print("Executivo"not in dicionarioSetores)
del dicionarioSetores["Executivo"]
print("Executivo" in dicionarioSetores)