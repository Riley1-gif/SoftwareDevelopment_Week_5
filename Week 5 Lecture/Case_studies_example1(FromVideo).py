import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    #give you results of the roll
    return roll


while True: #never ending loop until the user enters a valid number of players
    players = input("Enter the number of players (1-4):")
    if players.isdigit(): #checks if the input is a number
        players = int(players) #converts the input to an integer
        if 2 <= players <= 4:
            break # exits the While loop if the number of players is valid
        else:
            print("Please enter a valid number of players (2-4).")  
    else:
        print("Please enter a valid number.")

max_score = 50
players_scores = [0 for _ in range(players)] #creates a list of scores for each player, initialized to 0


while max(players_scores) < max_score: #continues the game until a player reaches the max score
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn.\n")
        print("Your current score is: ", players_scores[player_index])
        curent_score = 0

        while True: #continues the player's turn until they choose to stop or roll a 1
            should_roll = input("Do you want to roll the dice? (yes/no): ")
            if should_roll.lower() != "yes" and should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:#if the player rolls a 1, their turn is over and they lose all points accumulated in that turn
                print("You rolled a 1! Your turn is over.")
                current_score = 0
                break
            else:
                curent_score += value
                print(f"You rolled a: {value}.")

                
            print("Your score is: ", curent_score)


        # After the player's turn is over, their score for that turn is added to their total score
        players_scores[player_index] += curent_score
        print(f"Player {player_index + 1}'s total score is: {players_scores[player_index]}")


max_score = max(players_scores)
winind_idx = players_scores.index(max_score)
print("PLayer number", winind_idx +1, "is the winnder with a score of: ", max_score)