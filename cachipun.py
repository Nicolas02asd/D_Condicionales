import random

mylist = ["piedra", "papel", "tijeras"]

computadora = random.choice(mylist)
cachipun = input("Tu jugada es ")

if cachipun not in mylist:
    print("Argumento inválido: Debe ser piedra, papel o tijera.") 
else:  
    print(f"Computadora jugo {computadora}") 
    
# Se desplazo el código para evitar que se imprima "ganaste" cuando se ingresa mal la jugada.
    if computadora == cachipun:
        print("Es un empate, sigue intentando.")
    elif (computadora=="tijeras")and(cachipun=="papel"):
        print("Gana la computadora, suerte la próxima.")
    elif (computadora=="piedra")and(cachipun=="tijeras"):
        print("Gana la computadora, suerte la próxima.")
    elif (computadora=="papel")and(cachipun=="piedra"):
        print("Gana la computadora, suerte la próxima.")     
    else:
        print("Ganaste!!")   

