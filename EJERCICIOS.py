'''
EJERCICIO 8 (SEMANA 1)
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre} bienvenido!")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el primer numero: "))

producto = numero1 * numero2

print(f"El producto de ambos numeros es: {producto}")
'''
'''
#ejercicio 9
base = float(input ("Ingrese la base: "))
altura = float(input ("Ingrese la altura: "))
radio = float(input("Ingrese el radio del circulo: "))

perimetro = (base * altura) * 2
area = base * altura
perimetrocirc = (radio * 3.1416) * 2
areacirc = (radio ** 2) * 3.1416

print("El perimetro del rectangulo es: ", perimetro)
print("El area del rectangulo es: ", area)
print("El perimetro del circulo es: ", perimetrocirc)
print("El area del circulo es: ", areacirc)
'''
'''
#ejercicio 10

num1 = float(input ("Ingrese el primer numero: "))
num2 = float(input ("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2

print("El resultado de la suma es: ", suma)
print("El resultado de la resta es: ", resta)
print("El resultado de la multiplicacion es: ", mult)
print("El resultado de la division es: ", div)
'''

#ejercicio 11

gradosfarh = float(input ("Ingrese los grados Fahrenheit: ")) 

celsius = (gradosfarh - 32) * (5/9)

print(f"La conversion de grados fahrenheit a celsiues es: {celsius:.2f} °C")

