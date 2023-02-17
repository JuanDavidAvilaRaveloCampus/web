# 9. Construya un algoritmo en Python, que permita ingresar la
# información de un empleado e imprima el nombre, los
# apellidos y la antigüedad. Los datos que se deben solicitar
# son los siguientes:
# *Nombre * Teléfono *Año de ingreso a la empresa
# *Apellidos *Edad.

name = input("Name: ")
lastName = input("Last Name: ")
secondSurname = input("Second surname: ")
age = input("Age: ")
phone = input("Number: ")
year = input("Year of income: ")

print("Hola " + name + " " + lastName + ", ya hemos corregido tu año de ingreso. Por favor confirme si está correcto:\nAño de ingreso: " + year )
