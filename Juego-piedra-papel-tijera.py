turno = 0
turno_max = 4
final = False


while not final and turno < turno_max:

    nombre1 = input("¿Cual sera el nombre del jugador 1?: ")
    nombre2 = input("¿Cual sera el nombre del jugador 2?: ")

    print("(Max 3 turno) Turno:" , turno)

    jugador1 = input("¿Que elije el jugador 1? ¿Piedra, Papel o tijera?: ")
    jugador2 = input("¿Que elije el jugador ? ¿Piedra, Papel o tijera?: ")
    


    if jugador1 == jugador2:
        print("Empate")

    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        print("Ganador: " , nombre1)
        final = True
    
    else:
        print("Ganador: " , nombre2)
        final = True

    turno += 1

    if not turno < turno_max:
        print("Game over")

   
   
    

 
 






        
    
        
