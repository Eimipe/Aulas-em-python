def main():
  num1 = 0
  text = ""

  print("Com licença, poderia preencher seus dados para validar sua entrada nesta sessão?")
  num1 = int(input("\nInforme sua idade: "))
  if num1 >= 18:
    print("Entrada permitida")
  elif num1 >= 16 and num1 < 18:
    print("Você possui algum acompanhante maior de idade?")
    text = input("Informe S para sim e N para não: ")
    if text == "S":
      print("Entrada permitida")
    elif text == "N":
      print("Entrada negada")
    else:
      print("Você não digitou uma opção válida")
      print("Entrada negada")

  else:
    print("Entrada negada")

    
    
  return 0
  
if __name__ == "__main__":
  main()