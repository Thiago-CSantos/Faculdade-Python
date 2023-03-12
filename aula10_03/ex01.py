# 1. Uma lista só pode conter números inteiros? VERDADEIRO
lista = [1, 2, 3, 6, 69, 44]
print(lista)





# 4. O que é impresso pelo trecho de código a seguir? 3.14
lista = [3, 69, "gato", [56, 57, 'cachorro'], [], 3.14, False]
print(lista[5])

# 7. O que é impresso pelo trecho de código a seguir? [1, 3, 5, 2, 4, 6]
lista = [1, 3, 5]
outraLista = [2, 4, 6]
print(lista + outraLista)

# 8. O que é impresso pelo trecho de código a seguir? [1, 3, 5, 1, 3, 5, 1, 3, 5]
lista = [1, 3, 5]
print(lista * 3)
print("aqui")

# 9. O que é impresso pelo trecho de código a seguir? [[], 3.14, False]
lista = [3, 69, "gato", [56, 57, 'cachorro'], [], 3.14, False]
print(lista[4:])

# 10. O que é impresso pelo trecho de código a seguir? [False, 4, 2, True, 8, 6, 5]
lista = [4, 2, 8, 6, 5]
lista.insert(2, True)
lista.insert(0, False)
print(lista)


