nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 6:
    print(f"APROVADO!!! Sua média é : {media:.2f}")
else:
    print(f"REPROVADO!!! Sua média é : {media:.2f}")
input()