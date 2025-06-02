def main():

  num1 = 0
  num2 = 0
  
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))

  if num1 > num2:
    print("O", num1, "é maior que", num2)
    print("A soma deles dá: ", num1 + num2)
  elif num1 < num2:
    print("O", num2, "é maior que", num1)
    print("A subtração deles dá: ", num1 - num2)
  else:
    print("Os números são os mesmos")
    print("O quadrado dele dá: ", num1 * num2 ,"²")
  return 0
  
if __name__ == "__main__":
  main()