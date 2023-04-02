dicionario = {}

while len(dicionario) < 2:
    nome = str(input('digite um nome:'))
    telefone =  input('numero telefone')
    dicionario[nome] = telefone

for i in dicionario:

    if(i.startswith('R')):
        print(dicionario.keys())


print(dicionario['nome'])


