from funciones import suma as oper_1, multiplicacion as oper_2

var_1 = int(input("Ingresar un primer valor: "))
var_2 = int(input("Ingresar un segundo valor: "))

sum = oper_1(var_1, var_2)
print(f"El restulado de sus dos valores es: {sum}")

mult = oper_2(var_1, var_2)
print(f"El resultado de la multiplicacion es: {mult}")