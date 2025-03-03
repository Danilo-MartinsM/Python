n = int(input("Quantos números você vai digitar? "))
vet = [0 for x in range (0, n)]
for i in range (0, n):
    vet[i] = int(input("Digite um número: "))

soma = vet
media = soma / n

print(f"Valores: {vet[i]}")
print(f"Soma: {soma}")
print(f"Media: {media}")