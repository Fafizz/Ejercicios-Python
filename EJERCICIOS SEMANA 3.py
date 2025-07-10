'''
1) Realizar un programa que reciba 3 notas y de acuerdo con el promedio
obtenido, diga la nota es sobresaliente, muy bueno, bueno, regular o aplazado
y si este aprobado.

nota1 = float (input("Ingrese la primera nota: "))
nota2 = float (input("Ingrese la segunda nota: "))
nota3 = float (input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 6:
    print(f"Tu nota es: {promedio} Bueno, estás aprobado")
elif promedio >= 4:
    print(f"Tu nota es: {promedio} Regular, estás desaprobado")
elif promedio >= 8:
    print(f"Tu nota es: {promedio} Muy bueno, estás aprobado")
elif promedio == 10:
    print(f"Tu nota es: {promedio} Sobresaliente, estás aprobado")
else:
    print(f"Tu nota es: {promedio} Aplazado, estás desaprobado")
'''

'''
2) Dado 3 números identifique cual es el mayor. Considere que los números
pueden ser iguales.


num1 = int (input("Ingrese el primer numero: "))
num2 = int (input("Ingrese el segundo numero: "))
num3 = int (input("Ingrese el tercer numero: "))

if num1 == num2 == num3:
    print("Los tres números son iguales.")
elif num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")
'''

'''
3) En una tienda efectúan un descuento a los clientes dependiendo del monto de
la compra. El descuento se efectúa en base al siguiente criterio.
Si el monto es menor a $500 no hay descuento
Si el monto esta comprendido entre $500 y $1000 inclusive descuento del 5%
Si el monto está comprendido entre $1000 y $7000 inclusive descuento del
11%
Si el monto está comprendido entre $7000 y $15000 inclusive descuento del
18%
Si el monto es mayor a $15000 descuento del 25%


monto = float (input("Ingrese el monto de la compra: $"))

if monto < 500:
    descuento = 0
elif monto <= 1000:
    descuento = 0.05
elif monto <= 7000:
    descuento = 0.11
elif monto <= 15000:
    descuento = 0.18
else:
    descuento = 0.25


monto_con_descuento = monto * descuento 
pago_total = monto - monto_con_descuento

print(f"Descuento aplicado: ${monto_con_descuento:.2f}")
print(f"Total a pagar: ${pago_total:.2f}")
'''

'''
4) Realizar un programa que dado el mes de año indicar la cantidad de días que
tiene el mismo.


mes = int (input("Ingrese el numero del mes (1 al 12): "))

if mes == 1 and 3 and 4 and 7 and 8 and 10 and 12:
    print(f"El mes {mes}, tiene 31 dias")
elif mes == 5 and 6 and 9 and 11:
    print(f"El mes {mes}, tiene 30 dias")
else:
    print(f"El mes {mes}, tiene 28 dias")
'''

'''
5) Realizar un programa que calcule la edad de una persona si tiene como dato
su año de nacimiento.


anio_nac = int (input ("Ingrese su año de nacimiento: "))

edad = 2025 - anio_nac

print(f"Su edad es: {edad} años")
'''

'''
6) Escribir un programa que le pida una palabra al usuario, para luego imprimirla
1000 veces, en una única línea, con espacios intermedios.


palabra = str (input ("Escriba la palabra que desee: "))

print((palabra + " ") * 1000)
'''

'''
7) Escribir un programa que imprima todos los números pares entre dos números
que se le pida al usuario.

num1 = int(input ("Ingrese el primer numero: "))
num2 = int(input ("Ingrese el segundo numero: "))

for numero in range(num1, num2 + 1):
    if numero % 2 == 0:
        print(numero)
'''

'''
8) Escribir un programa que permita al usuario ingresar un conjunto de notas,
preguntando a cada paso si desea ingresar más notas, e imprimiendo el
promedio correspondiente


def ingresar_notas():
    notas = []
    
    while True:
        try:
            nota = float(input("Ingrese una nota (entre 0 y 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("La nota debe estar entre 0 y 10.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        continuar = input("¿Desea ingresar otra nota? (s/n): ").strip().lower()
        if continuar != 's':
            break

    if notas:
        promedio = sum(notas) / len(notas)
        print(f"\nPromedio de notas: {promedio:.2f}")
    else:
        print("\nNo se ingresaron notas.")

# Ejecutar el programa
ingresar_notas()

'''


'''
9) Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo, de altura el número
introducido.


def dibujar_triangulo():
    try:
        altura = int(input("Ingrese un número entero para la altura del triángulo: "))
        if altura <= 0:
            print("Por favor, ingrese un número entero positivo.")
            return

        for i in range(1, altura + 1):
            print("*" * i)

    except ValueError:
        print("Debe ingresar un número entero válido.")

# Ejecutar el programa
dibujar_triangulo()
'''

'''
10) Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.


def cont_letra():
    frase= input("Ingrese una frase: ")
    letra= input("Ingrese la letra que quiere buscar: ")

    if len == 1:
        print("Caracter invalido, ingrese una letra: ")
        return

cantidad = frase.count(letra)
print(f"La letra {letra} aparece {cantidad} veces en la frase")

cont_letra()

'''

