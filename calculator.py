import os

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num1 == 0:
        print("No se puede hacer una division entre 0")
        num2 = 1
    return num1 / num2
           

def return_values():
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numeros: "))
    return [num1, num2]

if __name__ == '__main__':
    message = f"Calculadora: \n Elige una opcion\n1 - Suma\n2 - Resta\n3 - Multiplicacion\n4 - Division\n5 - Salir\n"
    while True:
        os.system('cls')
        opcion = int(input(message))
        #Comparar cada una de las opciones y llamar a la funcion que corresponda
        if opcion == 1:
            numeros = return_values()
            resultado_suma = suma (numeros[0], numeros[1])
            print("El resultado de la suma es", resultado_suma)
        elif opcion == 2:
            numeros = return_values()
            resultado_resta = resta (numeros[0], numeros[1])
            print("El resultado de la resta es", resultado_resta)
        elif opcion == 3:
            numeros = return_values()
            resultado_multiplicacion = multiplicacion (numeros[0], numeros[1])
            print("El resultado de la multiplicacion es", resultado_multiplicacion)
        elif opcion == 4:
            numeros = return_values()
            resultado_division = division (numeros[0], numeros[1])
            print("El resultado de la division es", resultado_division)
        elif opcion == 5:
            print("Bye!")
            break
        else: 
            print("Opción Incorrecta")
            