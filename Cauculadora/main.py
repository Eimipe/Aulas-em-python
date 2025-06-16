from Soma import soma
from Sub import sub
from Multi import multi
from Div import div
def main():
    continuar = True
    while continuar:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite um numero: "))
        
        print("selecione: \n1 para somar \n2 para subtrair\n3 para multiplicar\n4 para dividir\n5 para sair")
        opcao = int(input("selecione: "))
        if opcao == 1:
            print(soma(num1,num2))
        elif opcao == 2:
            print(sub(num1,num2))
        elif opcao == 3:
            print(multi(num1,num2))
        elif opcao == 4:
            print(div(num1,num2))
        else:
            continuar = False

        print("\n\n")
    return 0
main()