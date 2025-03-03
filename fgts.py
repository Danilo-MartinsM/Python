horas = int(input())
valor_hora = float(input())

salarioB = horas * valor_hora 

if salarioB >= 0 and salarioB <= 900:
    print("voce é isento")
elif salarioB > 900 and salarioB <= 1500:
    salarioL = salarioB * 95/100
    print(f"seu salario bruto é { salarioB} houve um desconto de 5%, salario liquido é {salarioL} ")
elif salarioB > 1500 and salarioB <= 2500:
    salarioL = salarioB * 90/100
    print(f"seu salario bruto é { salarioB} houve um desconto de 10%, salario liquido é {salarioL} ")
elif salarioB > 2500:
    salarioL = salarioB * 80/100
    print(f"seu salario bruto é { salarioB} houve um desconto de 20%, salario liquido é {salarioL} ")
    