while True:
    nome = input("Digite um nome com mais de 3 caracteres: ")
    if len(nome) > 3:
        print("Nome válido!")
        break
    else:
        print("Nome invalido, com pelo menos 4 caracteres")

while True:
    idade = int(input("Digite uma idade entre 0 e 150: "))
    if idade >= 0 and idade <= 150:
        print("Idade válida!")
        break
    else :
        print("Idade invalida, digite uma idade entre 0 e 150")
while True:
    salario = float(input("Digite um salario maior que 0: "))
    if salario > 0:
        print("Salario valido!")
        break
    else :
        print("Salario invalido, Digite um salario maior que 0")
while True:
    sexo = input("Digite o sexo entre (f) ou (m): ")
    if sexo == "f" or "m":
        print("Sexo válido!")
        break
    else:
        print("Sexo invalido, coloque (f) ou (m)")
while True:
    estado_civil = input("Digite seu estado civil entre (s), (c), (v), (d): ")
    if estado_civil in ["s", "c", "v", "d"]:
        print("Estado civil válido!")
        break
    else:
        print("Digite um estado civil válido")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")