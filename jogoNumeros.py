import random 
numero_aleatorio = random.randrange(0, 100)
minimo = 0
maximo = 100
while True:
    chute = int(input(f"Digite um número entre {minimo} e {maximo}: "))
    if chute < minimo or chute > maximo:
        print("Fora do alcance")
        continue
        
    if chute > numero_aleatorio:
        maximo = chute
    elif chute < numero_aleatorio:
        minimo = chute
    else:
        print("Correto!")
        break
    perda = maximo - minimo
    if perda == 2:
        print("Perdeu playboy")
        break