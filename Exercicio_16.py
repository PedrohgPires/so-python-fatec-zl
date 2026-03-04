#Declaração de variaveis 
Horas: float = 0
VHora: float = 0
Percentual: float = 0
NumDependencias: int = 0
Salario: float = 0
Salarial: float = 0
Resultado: float = 0
#Inicio
Horas = float(input("Digite a quantidade de horas trabalhadas:"))
VHora = float(input("Digite o valor por hora:"))
Percentual = float(input("Digite o percentual de desconto:"))
NumDependencias = float(input("Digite o numero de dependencias:"))
Salario = (Horas*VHora)
Salarial = (Salario - ((Salario*Percentual)/100))
Resultado = (NumDependencias*100)+Salarial
print("O salário a receber é de =",Resultado,"Reais")
#Fim