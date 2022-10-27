#pede o nome do aluno e sua nota (de 0 a 10)e, se ele tirou nota 10, mostra "Você é bichão mesmo!"

nome = input("Qual é o nome do aluno? ")
nota = float(input("Qual é a nota? "))

if (nota == 10):
  print(f"{nome}, Você é o bichão mesmo!")
elif(nota >= 6 and nota <10):
  print(f"{nome}, bom trabalho. ")
else:
  print("Que burro, dá zero pra ele...")