import random

opciones = ["Piedra","Papel","Tijera"]

entrada_humano = 4
puntaje_computadora = 0
puntaje_jugador = 0
ronda = 1

GanarPerder = False
Empate = False

while(True):

  # Información de inicio
  print(f"\nRonda {ronda}")
  print(f"Tu puntaje: {puntaje_jugador}")
  print(f"Bot puntaje: {puntaje_computadora}")
  print("")

  # Selección de piedra-papel-tijera
  while entrada_humano > 3: 
    entrada_humano = int(input("¿Que escoges?\n1) Piedra\n2) Papel\n3) Tijera\n")) - 1
  
  # Selección de la computadora
  entrada_computadora = random.randint(0,2)
  
  # Muestra ambas selecciones
  print("")
  print(f"Seleccionaste: {opciones[entrada_humano]}")
  print(f"La computadora seleciono: {opciones[entrada_computadora]}")
  print("")

  # Funcionalidad de empate
  if (opciones[entrada_humano] == opciones[entrada_computadora]):
    Empate = True
    print("Empate\n")

  # Funcionalidad de ganar o perder
  if (opciones[entrada_humano] == "Piedra"):
    if (opciones[entrada_computadora] == "Tijera"):
      GanarPerder = True
  elif (opciones[entrada_humano] == "Papel"):
    if (opciones[entrada_computadora] == "Piedra"):
      GanarPerder = True
  else:
    if (opciones[entrada_computadora] == "Papel"):
      GanarPerder = True
  
  # Información de ganar o perder
  if(GanarPerder == True and Empate == False):
    print("Ganaste ¡Bien hecho!\n")
    puntaje_jugador = puntaje_jugador + 1
    GanarPerder = False
  elif GanarPerder == False and Empate == False:
    print("Perdiste ¡Suete la próxima!\n")
    puntaje_computadora = puntaje_computadora + 1

  ronda = ronda + 1   
  
  # Continuar junado o no
  if (True if int(input("¿Seguir jugando?\n1) Continuar\n2) Terminar\n")) - 1 == 0 else False) == False:
    print(f"\nRonda {ronda}")
    print(f"Tu puntaje: {puntaje_jugador}")
    print(f"Bot puntaje: {puntaje_computadora}")
    print("Gracias por jugar")
    break
