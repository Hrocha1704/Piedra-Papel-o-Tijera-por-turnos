turno = 0
turno_max = 4
final = False


while not final and turno < turno_max: #IMPORTANTE DETERMINAR LAS VARIABLES QUE DETERMINAN LA VICTORIA DENTRO DEL BUCLE PARA QUE ESTAS VAYAN CAMBIANDO SEGUN LOS RESULTADOS. SINO SE CREA BUCLE INFINITO

    nombre1 = input("¿Cual sera el nombre del jugador 1?: ") 
    nombre2 = input("¿Cual sera el nombre del jugador 2?: ")

    print("(Max 3 turno) Turno:" , turno)

    jugador1 = input("¿Que elije el jugador 1? ¿Piedra, Papel o tijera?: ")
    jugador2 = input("¿Que elije el jugador ? ¿Piedra, Papel o tijera?: ")
    


    if jugador1 == jugador2:
        print("Empate")

    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        print("Ganador: " , nombre1)
        final = True  #IMPORTANTE DEFINIR EL BOOLEANO = TRUE EN TODAS LAS POSIBILIDADES DE VICTORIA
    
    else:
        print("Ganador: " , nombre2)
        final = True #IMPORTANTE DEFINIR EL BOOLEANO = TRUE EN TODAS LAS POSIBILIDADES DE VICTORIA

    turno += 1   #PONER LA SUMATORIA A LO ULTIMO DEL CODIGO PARA QUE SE VAYA SUMANDO DESPUES DE UN TURNO, IMPORTANTE RESPETAR EL ORDEN DEL CODIGO EN PYTHON

    if not turno < turno_max:
        print("Game over")

   
   
    

 
 






        
    
        
