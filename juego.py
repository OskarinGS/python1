# Scrip de piedra papel o tijera con el usuario
import random
#Leer eleccion del usuario
user = input("Elige: Piedra, Papel o Tijera \n")
#Generar eleccion de la maquina
aleatorio = random.randint(1, 3)
if aleatorio == 1:
    machine = "Piedra"
elif aleatorio == 2:
    machine = 'Papel'
else:
    machine = 'Tijera'    

#Comparar para determinar quien gana
print (f"El usuario eligió {user} y la maquina eligió {machine}")
if machine == "Piedra" and user == "Papel":
    print("Ganaste")
elif machine == "Papel" and user == "Tijera":
    print("Ganaste")
elif machine == "Tijera" and user == "Piedra":
    print("Ganaste")   
elif machine == "Piedra" and user == "Tijera":
    print("Perdiste") 
elif machine == "Papel" and user == "Piedra":
    print("Perdiste")
elif machine == "Tijera" and user == "Papel":
    print("Perdiste")     
elif machine == user:
    print("Empate")    




