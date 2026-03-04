#Declaração de variaveis 
Tempo: float = 0
Vmedia: float = 0
Litros: float = 0
Distancia: float = 0
#Inicio
Tempo = float(input("Digite quanto tempo se passou:"))
Vmedia = float(input("Digite o valor da velocidade media:"))
Distancia = Vmedia*Tempo
Litros = Distancia/12
print("A quantidade de litros gastos nessa viagem é de =",Litros,"Litros")
#Fim