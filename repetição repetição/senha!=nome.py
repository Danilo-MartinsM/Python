nome = input("Digite seu nome: ")
while True:
    senha = input("Digite sua senha: ")
    if senha != nome:
        print("Sua senha foi salva!")
        break
    else :
        print("Digite uma senha diferente do seu nome")