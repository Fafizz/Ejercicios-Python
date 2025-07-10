#Tamagotchi

nombre = str()
suenio = 0
hambre = 0
animo = 5
salud = 5
esta_vivo = True

print("TAMAGOTCHI ALPHA 0.10")
menu = 7

while menu != 6 and esta_vivo:
    print("0- Nuevo")
    print("1- Mostrar estado")
    print("2- Alimentarlo")
    print("3- Dormir")
    print("4- Jugar")
    print("5- Medicina")
    print("6- Salir")
    print("7- ¡EXPLOTAR!")

    opcion = int (input ("Ingrese una opcion (0 al 7): "))
    while opcion < 0 or opcion > 7:
        opcion = int(input("Opcion no valida, ingrese un numero del 0 al 6: "))

    if opcion == 0:
        nombre = input("Ingrese el nombre de su mascota: ")
        suenio=0
        hambre=0
        animo=5
        salud=5
    elif opcion ==1: #estado
        print(f"Nombre: {nombre} Suenio: {suenio} Hambre: {hambre} Animo: {animo} Salud: {salud}")
    elif opcion ==2: #hambre
        hambre -=5
        suenio +=5
        salud +=1
        animo +=2
    elif opcion ==3: #dormir
        suenio -=5
        hambre +=5
        animo -=2
    elif opcion ==4: #jugar
        suenio +=5
        hambre +=5
        animo +=5
        salud -=1
    elif opcion ==5: #medicina
        salud += 5
    elif opcion ==7:
        salud -= 30


    if suenio > 30 or hambre > 30 or animo <= 0  or salud <= 0:
        print(f"{nombre} QDEP :(") 