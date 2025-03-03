quantidade = int(input("Quantos números serão digitados? "))
soma = 0
for i in range(0, quantidade):
    x = int(input("Digite um número: "))
    soma = soma + x

print(f"Soma: {soma}")
input()