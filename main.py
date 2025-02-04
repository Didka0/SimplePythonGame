import random

def print_game_rules():
    print("Rules: \n Each player can choose one of those commands to do on his turn:")
    print("Attack ( Deals a random number damage from 10 to 20 to the other player )")
    print("Heal ( Heals 10 health )")
    print("Cast fireball ( Costs 40 mana and deals 30 damage to the other player )")
    print("Restore mana ( Restores 20 mana )")

def player1_turn():
    name1 = input("\n Enter your name,Player 1: ")
    print("Choose your move,", name1,":", end='')
    player_choice1 = input(" Attack,Heal,Cast fireball or Restore mana? ")

    if player_choice1 == "Attack":
        print("You dealt: ",random.choice(range(10, 20)), " damage")

def main():
    print_game_rules()

    answer = input("\n Let's start?: ")

    answer = answer.lower()

    if answer == "yes":
        print("\nPlayers info: \n Player 1 health - 100 \n Player 1 mana - 100 \n \n Player 2 health - 100 \n Player 2 mana - 100")
    else:
        print("See you later!")
        exit()

    player1_turn()

main()

