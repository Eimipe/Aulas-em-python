def main():
  num1 = 1
  num2 = 2

  print("Hello World", num1)
  print("Hello World", num2)

  num1 = int( input("\nDigite o primeiro número: "))
  num2 = int( input("Digite o segundo número: "))

  print("\nHello World", num1)
  print("Hello World", num2)

  soma = num1 + num2
  sub = num1 - num2
  mult = num1 * num2
  
  #se a variavel num2 for igual a zero ele dirá que nao e possivel dividir caso o contrario efetua a divisao normalmente
  
  if num2 == 0:
    print("Não é possível dividir por zero")
    div = ("erro")
  else:
    div = num1 / num2
  
  print("A soma de", num1 ,"por", num2 ,"é:", soma)
  print("A subtração de", num1 ,"por", num2 ,"é:", sub)
  print("A multiplicação de", num1 ,"por", num2 ,"é:", mult)
  print("A divisão de", num1 ,"por", num2 ,"é:", div)

  if soma == 24: print("Lá ele")
  if sub == 24: print("Lá ele")
  if mult == 24: print("Lá ele")
  if div == 24: print("Lá ele")

  #if soma == 24 or sub == 24 or mult == 24 or div == 24: print("Lá ele")  # Outra forma de fazer
  return 0
  
if __name__ == "__main__":
  main()