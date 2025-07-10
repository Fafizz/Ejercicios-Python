'''
1. Mostrar los números ascendentes desde el 1 al 10

for i in range (1,11):
    print(i)
'''

'''
2. Mostrar los números descendentes desde el 10 al 1


for i in range (11, 1, -1):
    print(i - 1)
'''

'''
3. Ingresar un número. Mostrar los números desde 0 hasta el número
ingresado.

numero = int(input("Ingrese un numero: "))

for i in range (0,numero + 1):
    print(i)

'''

'''
4. Se ingresan un máximo de 10 números o hasta que el usuario ingrese
el número 0. Mostrar la suma y el promedio de todos los números.


suma = 0
cont = 0

for i in range (10):
    numero = int(input(f"Ingrese el numero {i + 1}: "))
    if numero == 0:
        break
suma = suma + numero
cont = cont + 1
promedio = suma / cont

print(f"La suma de los numeros es: {suma}")
print(f"El promedio de los numeros es: {promedio}")
'''

'''
5. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

for i in range(1,10):
    if i % 3 == 0:
        print("Los multiplos de 3 entre 1 y 10 son: ", i)

'''

'''
6. Mostrar los números pares que hay desde la unidad hasta el número
50 (*)

for i in range(1,50):
    if i % 2 == 0:
        print("Los numeros pares hasta el 50: ", i)
'''


'''
7. Ingresar un número. Mostrar todos los divisores que hay desde el 1
hasta el número ingresado. Mostrar la cantidad de divisores
encontrados.


numero = int(input("Ingresa un número: "))

contador = 0
print(f"Divisores de {numero}:")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
        contador += 1

print(f"Cantidad de divisores encontrados: {contador}")
'''


'''
8. Ingresar un número. Determinar si el número es primo o no.


numero = int(input("Ingresa un número: "))

if numero <= 1:
    print("No es primo")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")

'''


'''
9. Ingresar un número. Mostrar cada número primo que hay entre el 1 y
el número ingresado. Informar cuántos números primos se
encontraron.


def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingresa un número: "))

contador = 0

print(f"Números primos entre 1 y {numero}:")
for num in range(1, numero + 1):
    if es_primo(num):
        print(num)
        contador += 1

print(f"Se encontraron {contador} números primos.")
'''


'''
10.Codificar un algoritmo que permita registrar de los empleados de una
empresa (no se sabe cuántos), su peso y saber cuántos pesan hasta
80kg inclusive y cuantos pesan más de 80 kg.


empleados = int(input("Cuantos empleados desea registrar?: "))

for i in range(0,empleados):
   nombre = (input(f"Ingrese su nombre empleado {i + 1}: "))
   peso = int(input("Ingrese su peso: "))

   if peso <= 80:
      print(f"Hay {i} empleados que pesan hasta 80 Kg")
   elif peso > 80:
      print(f"Hay {i} empleados que pesan mas de 80 Kg")
    
'''


'''
11.Se registran de los empleados de una empresa numero de legajo,
nombre, sueldo y sexo 1 femenino,2 masculino, 3 otro. Diseñar un
programa que permita informar cuantas mujeres ganan más de
300000y cuantos hombres ganan menos de 200000.
'''
legajo = []
nombre = []
sexo = [1,2,3]
sueldo = []


empleados = int(input("Cuantos empleados desea registrar?: "))

for i in range(0,empleados):
    legajo = int(input(f"Ingrese su numero de legajo, empleado {i+1}: "))
    nombre = (input(f"Ingrese su nombre, empleado {i+1}: "))
    sexo = int(input(f"Ingrese su sexo, empleado {i+1}: 1- Femenino, 2- Masculino, 3- Otro: "))
    sueldo = int(input(f"Ingrese su sueldo, empleado {i+1}: "))


print(f"Legajo: {legajo}, Nombre: {nombre}, Sexo: {sexo}, Sueldo: {sueldo}")

if sexo == 1 and sueldo > 300000:
    print(f"Hay {i} que ganan mas de 300K")
elif sexo == 2 and sueldo < 200000:
    print(f"Hay {i} hombres que ganan menos de 200k")