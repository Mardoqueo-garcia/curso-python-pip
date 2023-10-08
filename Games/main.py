import random
opciones = ['piedra','papel','tijera']
empates_count = 0
user_win = 0
user_luser = 0
rounds = 0

name = input('Cual es tu nombre? == > ')

print(f"\n Oye {name.upper()}\n Jugamos piedra, papel o tijera, Aceptas el reto?? ")
resp_user = input("Si o No  ")
resp_user.lower()

while resp_user == "si" or resp_user == "s":
    opcion_user = input("Elige: ==> Piedra, Papel o Tijera ")
    opcion_user.lower()
    rounds +=1
    while not opcion_user == "piedra" or not opcion_user == "papel" or not opcion_user == "tijera":
        opcion_compu = random.choice(opciones)
        #Por si da empate
        if opcion_user == opcion_compu:
            print(f"\nHas elegido : {opcion_user}")
            print(f"La computadora ha elegido: {opcion_compu}")
            print("Uppps, quedaron empatados.")
            empates_count +=1
            break
        #por si el usuario elige tijera
        elif opcion_user == "tijera":
            if opcion_compu == 'piedra':
                print(f"\nHas elegido : {opcion_user}")
                print(f"La computadora ha elegido: {opcion_compu}")
                print("Lo siento, te gano la computadora")
                user_luser +=1
            else:
                print(f"\nHas elegido : {opcion_user}")
                print(f"La computadora ha elegido: {opcion_compu}")
                print("Felicidades, has ganado la ronda")
                user_win +=1
            break
        #si el usuario elige piedra
        elif opcion_user == "piedra":
            if opcion_compu == 'tijera':
                print(f"\nHas elegido : {opcion_user}")
                print(f"La computadora ha elegido: {opcion_compu}")
                print("Felicidades, has ganado la ronda")
                user_win +=1
            else:
                print(f"\nHas elegido : {opcion_user}")
                print(f"La computadora ha elegido: {opcion_compu}")
                print("Lo siento, te gano la computadora")
                user_luser +=1
            break
        #Si el usuario elige papel
        elif opcion_user == "papel":
            if opcion_compu == 'tijera':
                print(f"\nHas elegido : {opcion_user}")
                print(f"La computadora ha elegido: {opcion_compu}")
                print("Lo siento, te gano la computadora")
                user_luser +=1
            else:
                print(f"\nHas elegido : {opcion_user}")
                print(f"La computadora ha elegido: {opcion_compu}")
                print("Felicidades, has ganado la ronda")
                user_win +=1
            break
        else : 
            print(f"\n{name.upper()} elegistes una opcion no válida, intenta de nuevo")
            opcion_user = input("Elige: ==> Piedra, Papel o Tijera ")
    print("\nJugamos otra ronda? ")
    resp_user = input("Si o No ==> ")
    resp_user.lower()

print("======" *15)
print(f"{name.upper()} tus rondas totales fuerón: {rounds} ")
print(f"Empates: {empates_count}, Derrotas: {user_luser}, Victorias: {user_win} ")
print (f"Gracias por jugar conmigo {name} :)")