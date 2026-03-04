#Declaração de variaveis 
Cateto1: float = 0
Cateto2: float = 0
Hipotenusa3: float = 0
#Inicio
from math import sqrt
Cateto1 = float(input("Digite o valor do primeiro cateto:"))
Cateto2 = float(input("Digite o valor do segundo cateto:"))
Hipotenusa3 = sqrt((Cateto1*Cateto1)+(Cateto2*Cateto2))
print ("o valor da hipotenusa é de =",Hipotenusa3)
#Fim