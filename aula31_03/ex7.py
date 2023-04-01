var_global = 10 #variavel global

def mult( num1, num2):
    var_local = num1 * num2
    print(var_local)

mult(2,3)

print(var_local) #irar dar erro ' name 'var_local' is not defined. Did you mean: 'var_global'? '