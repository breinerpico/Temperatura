import math

#input
C = input("Digite la cantidad de grados C a convertir")
C = int(C)

#processing
F = (C*(9/5))+32
K = C + 273.15

#output
print("grados farenheit: " + str(F))
print("grados kelvin: " + str(K))
