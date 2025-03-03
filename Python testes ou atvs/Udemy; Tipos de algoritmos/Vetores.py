n = int(input("Quantos números você vai digitar? "))
lista = [0 for x in range(n)]
for i in range (0, n):
    lista[i] = float(input("Digite um número: "))

print()
print("Números digitados: ")
for i in range (0, n):
    print(f"{lista[i]:.1f}")

input()