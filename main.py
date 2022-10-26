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