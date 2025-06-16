import random


def main():

  Notas = [0.0] * 4
  i = 0
  while i < 4:
    Notas[i] = random.uniform(0.0, 10.0)
    i += 1

  Media = (Notas[0] + Notas[1] + Notas[2] + Notas[3]) / 4.0

  print(
      f"Notas:, {Notas[0]:,.2f}, {Notas[1]:,.2f}, {Notas[2]:,.2f}, {Notas[3]:,.2f}"
  )
  print(f"Média:, {Media:,.2f}")

  if Media >= 6.0:
    print("Aprovado")
  elif Media >= 4.0:
    print("Recuperação")
  else:
    print("Reprovado")

  return 0


main()
