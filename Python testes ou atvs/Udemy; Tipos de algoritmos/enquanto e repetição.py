numero = int(input("Digite o primeiro número: "))
soma = 0

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite outro numero: "))

print(f"Soma: {soma}")
input()