nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

media_idade = (idade1 + idade2) / 2

print("Dados da primeira pessoa: ")
print(f"Nome: {nome1}")
print(f"Idade: {idade1}")
print("Dados da segunda pessoa: ")
print(f"Nome: {nome2}")
print(f"Idade: {idade2}")
print(f"A idade média de {nome1} e {nome2} é de {media_idade} anos ")
input()