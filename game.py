import random

opciones = ["piedra", "papel", "tijera"]

def play():
    while True:
        game_to_guess = random.choice(opciones)
        my_game = input("Elige piedra, papel o tijera: ")
        
        print(f"Tú elegiste: {my_game}")
        print(f"La máquina eligió: {game_to_guess}")
        print("--- VERSUS ---")

        if my_game == game_to_guess:
            print("¡Empate! Volvamos a jugar.")
            
        elif (my_game == "piedra" and game_to_guess == "tijera") or \
             (my_game == "papel" and game_to_guess == "piedra") or \
             (my_game == "tijera" and game_to_guess == "papel"):
            print("¡Ganaste la ronda!")
            break
            
        else:
            print("¡Perdiste! Inténtalo de nuevo.")
            
        print("==============================\n")

play()
