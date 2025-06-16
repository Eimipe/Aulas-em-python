from verificarZero import verificarZero
def div(num1,num2):
    if verificarZero(num2):
        div = "Divisão por zero é impossivel"
    else:
        div = num1/num2
    return div



    