# 8. Escriba un bloque cualquiera de código en Python en donde
# utilice 2 condicionales (if) anidados.

from random import randint, random, uniform

num1 = randint(1, 10)
num2 = randint(1, 10)

# # # # num2 = randint(1, 10)

if num1 == num2:
    print(f"\n Hay un empate")
if num1 > num2:
    print(f"\n num1 es mayor a num2")
    if num1 < num2:
        print(f"\n num1 es menor a num2")
else:
    print(f"\n El numero es irreal")
