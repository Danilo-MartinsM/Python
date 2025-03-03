from datetime import datetime

nome = input("digite o seu nome: ")
data_nascimento_str = input("Digite a sua idade (ex: dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')

def calcularIdade(idade):
    dataAtual = datetime.now()
    idade = dataAtual.year - data_nascimento.year - ((dataAtual.month, dataAtual.day) < (data_nascimento.month, data_nascimento.day))
    return idade

idade = calcularIdade(data_nascimento)
print(f"{nome}, você tem {idade} anos")