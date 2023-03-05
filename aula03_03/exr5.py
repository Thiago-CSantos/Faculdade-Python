texto=  'como pegar o tamanho de uma string em python'

print(texto.startswith("como"))
print(texto.endswith('python'))

x ="tamanho" in texto
print(x)

y ="tamanho" not in texto
print(y)

print(texto.upper())
print(texto.lower())