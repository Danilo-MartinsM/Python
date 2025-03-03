l = int(input("Quantas linhas vão ter na matriz? "))
c = int(input("Quantas colunas vão ter na matriz? "))

mat = [[0 for x in range (c)]for x in range (l)]
for i in range (0, l):
    for j in range (0, c):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("Matriz digitada: ")
for i in range (0, l):
    for j in range (0, c):
        print(f"{mat[i][j]} ", end = "")
    print()
input()