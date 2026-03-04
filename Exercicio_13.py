#Declaração de variaveis 
Quilos: float = 0
Dias: int = 0
#Inicio
Quilos = float(input("Digite a quantidade de alimento em quilos:"))
Dias = (Quilos*1000)/50
print ("Consumindo 50g por dia, essa quantidade durará",Dias," dias")
#Fim