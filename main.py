def print_game_rules():
    print("Rules: \n Each player can choose one of those commands to do on his turn:")
    print("Attack ( Deals a random number damage from 10 to 20 to the other player )")
    print("Heal ( Heals 10 health )")
    print("Cast fireball ( Costs 40 mana and deals 30 damage to the other player )")
    print("Restore mana ( Restores 20 mana )")

def main():
    print_game_rules()

    answer = input("Let's start?: ")

    answer = answer.lower()

    if answer == "yes":
        print("Players info: \n Player 1 health - 100 \n Player 1 mana - 100 \n \n Player 2 health - 100 \n Player 2 mana - 100")
    else:
        print("See you later!")
        exit()
    
main()

