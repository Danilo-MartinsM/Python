velociadeInicial = int(input("Digite o valor da velocidade inicial (m/s): "))
tempo = int(input("Digite o tempo (em segundos): "))
gravidade = 10

distancia = velociadeInicial * tempo + (gravidade * tempo ** 2) / 2

print(f"Valor da distância: {distancia}")