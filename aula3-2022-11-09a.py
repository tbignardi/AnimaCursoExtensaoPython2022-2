print("Início da aula 3 (09/11/2022")

contador = 1

#exibir de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador +1 #contador += 1



#laço for (python for = for each)
fruta = "morango"
#print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "melancia"

#lista
frutas = ["morango", "laranja", "melancia"]

#quero exibir apenas a 3a. fruta (melancia)
print(frutas[2])

#exibir quantas frutas tem na minha lista?
print(len (frutas)) #length = tamanho

#quero incluir uma fruta nova
frutas.append("manga")

#print(frutas[0])
#print(frutas[1])
#print(frutas[2])
#print(frutas[3])
#print(frutas[4])

print("Exemplo das frutas com while: ")

frutas.append("jabuticaba")
i = 0 #(i significa index)
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)