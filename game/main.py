import random
'''
Piedra, Papel o Tijera

Piedra gana a Tijeras
Papel gana a Pedra
Tijeras gana a Papel
'''

def game(user_option, round, round_counts):
  # get pc option for the game
  game_options = ("piedra", "papel", "tijeras")
  pc_option = random.choice(game_options)
  user_option_name = game_options[user_option - 1]

  print("Elegiste ", user_option_name.capitalize())
  print("La PC eligió", pc_option.capitalize())

  # Evaluamos   si es empate.
  if pc_option == user_option_name:
    print("Empate :| en la ronda #", round)
    return round_counts

  # Evaluamos Piedra
  option = game_options[0]  # Piedra
  if pc_option == option:
    if user_option_name == "papel":
      round_counts["user"] += 1
      print("Ganaste :D en la ronda #", round)
    else:
      round_counts["pc"] += 1
      print("Perdiste D: en la ronda #", round)

  # Evaluamos Papel
  option = game_options[1]  # Papel
  if pc_option == option:
    if user_option_name == "tijeras":
      round_counts["user"] += 1
      print("Ganaste :D en la ronda #", round)
    else:
      round_counts["pc"] += 1
      print("Perdiste D: en la ronda #", round)

  # Evaluamos Tijeras
  option = game_options[2]  # Tijeras
  if pc_option == option:
    if user_option_name == "piedra":
      round_counts["user"] += 1
      print("Ganaste :D en la ronda #", round)
    else:
      round_counts["pc"] += 1
      print("Perdiste D: en la ronda #", round)

  return round_counts


def get_user_choice():
  # get user option
  print("Piedra = 1")
  print("Papel = 2")
  print("Tijeras = 3")

  while True:
    user_option = input("Elije tu opción para jugar: ")

    if user_option.isdigit():
      user_option = int(user_option)
      if user_option >= 1 and user_option <= 3:
        break

    print(f"{user_option} no esta dentro del juego :(")

  return user_option


def check_winner(total_user, total_pc):
  resp = False
  if (total_user == 2 or total_pc == 2):
    print("==" * 10, "Puntaje Total", "==" * 10)
    print("Obtuviste ", total_user, " puntos.")
    print("La pc obtuvo ", total_pc, " puntos.")
    if (total_user == 2):
      print("Ganaste :D el juego!")
      resp = True
    else:
      print("Perdiste :D el juego!")
      resp = True

  return resp


def start_game():
  round = 0
  round_counts = {"user": 0, "pc": 0}
  while round_counts["user"] < 2 and round_counts["pc"] < 2:
    round += 1
    print("==" * 10, "Round #", round, "==" * 10)
    usr_option = get_user_choice()
    round_counts = game(usr_option, round, round_counts)

    is_there_a_winner = check_winner(round_counts["user"], round_counts["pc"])
    if (is_there_a_winner):
      break


start_game()
