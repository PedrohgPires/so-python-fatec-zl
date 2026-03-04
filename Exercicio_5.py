#Declaração de variaveis 
a: float = 0
b: float = 0
c: float = 0
Delta: float = 0
x1: float = 0
x2: float = 0
#Inicio
from math import sqrt
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))
Delta = (b*b)-4*a*c
x1 = (-b+ sqrt(Delta))/2*a
x2 = (-b- sqrt(Delta))/2*a
print ("A primeira raiz é de =",x1)
print ("A segunda raiz é de =",x2)
#Fim