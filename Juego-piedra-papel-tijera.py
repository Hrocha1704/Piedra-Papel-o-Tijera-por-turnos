turno = 0
turno_max = 4
final = False


while not final and turno < turno_max:
    print("(Max 3 turno) Turno:" , turno)

    jugador1 = input("Piedra, Papel o tijera: ")
    jugador2 = input("Piedra, Papel o tijera: ")


    if jugador1 == jugador2:
        print("Empate")

    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        print("Gana Jugador 1")
        final = True
    
    else:
        print("Gana jugador 2")
        final = True

    turno += 1

    if not turno < turno_max:
        print("Game over")

   
   
    

 
 






        
    
        
