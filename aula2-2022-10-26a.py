#aula2 26-10-2022

# comando input(): quero permitir que o usuário digite algo
nome = input("Digite seu nome: ")

#comando de saída: exibir na tela
#print(nome)
print(f"Boa noite, seu nome é {nome}")

#para pedir a idade para o usuário
idade = int(input("Digite sua idade: "))
#exibir a idade na tela
print(f"Boa noite, seu nome é {nome} e sua idade é {idade}")

#e se eu quisesse exibir o dobro da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#estrutura condicional - if
#se a pessoa for maior de idade, mostre "Você é maior de idade!"
if (idade >= 18):
  print("Você é maior de idade! ")
else:
  print("Você é menor de idade.")

  #e se eu quisesse perguntar o gênero (M = Masculino e F = Feminino)
  #mostre (... e você também precisa/precisou prestar o serviço militar obrigatório)
#fora do escopo do if, não está indentada

genero = input("Qual o seu gênero? M = Masculino, F = Feminino, O = Outros: \n ")
if(idade >= 18 and genero == "M"):
  print("Você precisa prestar o serviço militar obrigatório .")

print("Isso vai ser executado de qualquer jeito")