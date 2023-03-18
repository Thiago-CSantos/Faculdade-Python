#ex3
categoria = int(input("Digite uma categoria do produto"))

if(categoria == 1):
    preco = 10
else:
    if(categoria ==2):
        preco = 18
    else:
        if(categoria ==3):
            preco = 23
        else:
            if(categoria ==4):
                preco = 25
            else:
                if(categoria ==5):
                    preco = 31
                else:
                    print("Categoria invalida, digite um valor 1 e 5")
                    preco = 0
print("O preco do produto é R$ {}" .format(preco))