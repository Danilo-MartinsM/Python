
while True: 
    nota = float(input("Digite uma nota de 0 a 10: "))
    if nota >= 0 and nota <= 10:
        print(f"Sua nota é: {nota}")
        break
    else:
        print("Digite uma nota válida!!")
