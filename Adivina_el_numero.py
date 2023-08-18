#Juego de adivina el numero
import random  #Libreria para generar numeros aleatorios

#Llama a la funcion jugar

print("Bienvenido al Juego adivina un numero del 1 al 5 ")
r = random.randint (1,5)   #Genera un numero entre [0 y N]
pista = r / 2
print("Pista el numero divido en cierto numero da: "+ str(pista))
n = int(input('Ingrese un número: '))

val = True
while val:#Bucle infinito
    if r == n :
        print ("Felicidades has acertado en",r,"intentos.")
        val = False
        break    #Si es igual sale del bucle  
    else:     #else se ejecuta si no hay error en la sentencia anterior
        print("Lo sentimos no ganaste")
    n = int(input('Ingrese otro número: '))    

        



