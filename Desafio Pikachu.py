def main():
  
  import random

  Notas = [0] * 4
  i = 0
  while i < 4:
    Notas[i] = random.randint(1, 10)
    i += 1

    Media = (Notas[0] + Notas[1] + Notas[2] + Notas[3])/4
    print("Notas:", Notas)
  
    print("Média:", Media)

    if Media >= 6:
      print("Aprovado")
    elif Media >= 4:
        print("Recuperação")
    else:
        print("Reprovado")
      
    
    
  return 0
  
if __name__ == "__main__":
  main()