import random

            # STATEMENTS

# Rounds won to finish
max_Victories_text = '¿Cuántas victorias para ganar el Juego? '

# Start of the round
chooseOne = "¿Piedra?, ¿Papel?, o ¿Tijera? => "

# Wrong Option
invalidOption = "Esa opción es INVÁLIDA. Escoge entre: "
invalidVictories = "Selecciona un número entre 1 y 10"

# Choices to play
option1 = "piedra"
option2 = "papel"
option3 = "tijera"

# What did each player choose
player1_option = 'Tu opción fue: '
player2_option = 'La compu jugó: '

# End of round declaration
user_Win = 'Has Ganado ¡Felicitaciones!'
pc_Win = 'Has Perdido, sigue intentando'
tie = '¡EMPATE!'

# End game Statement
youWin1 = 'HAS GANADO '
youWin2 = ' rondas. La victoria es tuya'

youLost1 = "HAS PERDIDO "
youLost2 = " rondas"

# End Game Summary Results
finalResult = " RESULTADO "

gamesPlayed = "Partidas Jugadas: "
finalWins   = "Victorias: "
finalLosses = "Derrotas: "

            # VARIABLES

options = (option1, option2, option3)

max_Victories   = 0

user_wins       = 0
computer_wins   = 0

count = 0

anotherGame = True

            # Pregunta inicial

max_Victories = int(input(max_Victories_text))
if (max_Victories < 1) or (max_Victories > 10):
    print(invalidVictories)

            # GAME STARTS

while anotherGame == True:
 
    # User Option
    print('')
    user_option = input(chooseOne)
    user_option = user_option.lower().strip()
    count += 1

    if not user_option in options:
        print(invalidOption, options)
        count -= 1

    # Opción de la Computadora
    computer_option = random.choice(options)

        # DECLARACIONES
  
    # THE SIGNATURE OF THE ROUND
    print('')
    print(player1_option, user_option)
    print(player2_option, computer_option)
    print('')
    print('*' * 5, finalResult, '*' * 5)
    print('')
    print('_' * 15)

            # GAME LOGIC

    # User Wins
    if (user_option == option1 and computer_option == option3) or (user_option == option2 and computer_option == option1) or (user_option == option3 and computer_option == option2):
        user_wins += 1
        print(user_Win)

    # Tie
    elif user_option == computer_option:
        print(tie)

    # Computer Wins
    else:
        computer_wins += 1
        print(pc_Win)
    
        # FINAL SIGNATURE WITH FINAL RESULTS    

    # Rounds Summary
    print('')
    print('-' * 20)
    print(gamesPlayed, count)
    print(finalWins, user_wins)
    print(finalLosses, computer_wins)
    print('-' * 20)

        # FINISH THE GAME
    
    # Break Condition
    if (user_wins == max_Victories) or (computer_wins == max_Victories):
        anotherGame = False
    
    # Break/Finish Conditions/Statements
        if user_wins == max_Victories:
            print('')
            print(' \ \   /\   / /  | |  |  \  | |')
            print('  \ \ /  \ / /   | |  |   \ | |')
            print('   \   /\   /    | |  | |\ \| |')
            print('    \_/  \_/     | |  | | \___|')
            print('')

            print(youWin1, max_Victories, youWin2)
        else:
            print('')
            print(youLost1, max_Victories, youLost2)
            print('')
    break
