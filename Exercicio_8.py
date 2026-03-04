#Declaração de variaveis 
Deposito: float = 0
Resultado: float = 0
Porcentagem: float = 0
#Inicio
Deposito = float(input("Digite o valor do deposito:"))
Porcentagem = (Deposito*0.013)
Resultado = (Deposito+Porcentagem)
print ("O seu valor após aplicação de 1,3% ao mês é de =",Resultado)
#Fim