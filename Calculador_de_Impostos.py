sal_hor = float(input("Quanto você ganha por hora? "))
horas = int(input("Número de horas trabalhadas por mês:"))
salario = sal_hor * horas
IR = (salario * 11/100)
INSS = (salario * 8/100)
Sind = (salario * 5/100)

salario_liq = salario - (IR + INSS + Sind)


print("Seu salário bruto é de = R$",salario)
print("Imposto de renda = R$",IR)
print("INSS = R$",INSS)
print("Contribuição pro sindicato = R$", Sind)
print("Seu salario liquido é = R$", salario_liq)