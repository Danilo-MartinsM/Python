print("Digite dois números: ")
n1 = int(input())
n2 = int(input())

if n1 > n2:
    troca = n1
    n1 = n2
    n2 = troca

soma = 0
for i in range(n1 + 1, n2):
    if i % 2 !=0:
        soma = soma + i

print(f"Soma dos impares: {soma}")
