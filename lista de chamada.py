def main():
  print("Lista de chamada")
  # jeitos de criar um vetor
  # sem valores, apenas tamanho
  # nome = [0] * 5
  # sem tamanho, apenas valores
  # nome = ["JAIR", "JOSE", "MARIA", "JOAO", "DOUGLAS"]
  
  i = int ( input("Quantos alunos tem na sala?: "))
  j = 0
  nome = [""] * i
  
  while j < i:
    nome[j] =  input("Qual é o nome do aluno?: ")
    j = j + 1
    
    print("Alunos presentes: ", nome,)
    
  return 0
  
if __name__ == "__main__":
  main()