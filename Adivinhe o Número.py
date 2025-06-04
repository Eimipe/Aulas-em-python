def main():
  
  import random
  
  numEsc = random.randint(1, 100)
  numDig = 0
  i = 0
  
  print("Escolhi um número entre 1 e 100!\n")
  
  while numDig!= numEsc:
    numDig = int(input("Digite um número: "))
    i += 1
    
    if numDig > numEsc:
      print("Você errou, Meu número é menor\n")
    
    elif numDig < numEsc:
      print("Você errou, Meu número é maior\n")
    
    else:
        print("\nParabéns! Você acertou! Meu número era: ", numEsc,"\nVocê prescisou de ", i,"tentativas")

    
  return 0
  
if __name__ == "__main__":
  main()