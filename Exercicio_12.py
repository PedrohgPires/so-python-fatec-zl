#Declaração de variaveis 
Ano: int = 0
AnoNasc: int = 0
Resultado: int = 0
Idade: int = 0
#Inicio
AnoNasc = int(input("Digite o seu ano de nascimento:"))
Ano = int(input("Digite o seu ano atual:"))
Idade = Ano-AnoNasc
Resultado = Idade + 17
print ("Você tem ",Idade,"anos")
print ("Daqui 17 anos você terá ",Resultado," anos")
#Fim