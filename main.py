import random

def print_game_rules():
    print("Rules: \n Each player can choose one of those commands to do on his turn:")
    print("Attack ( Deals a random number damage from 10 to 20 to the other player )")
    print("Heal ( Heals 10 health )")
    print("Cast fireball ( Costs 40 mana and deals 30 damage to the other player )")
    print("Restore mana ( Restores 20 mana )")

def print_stats(stats):
    print("\nPlayers info: \n Player 1 health - {player1_health} \n Player 1 mana - {player1_mana} \n \n Player 2 health - {player2_health} \n Player 2 mana - {player2_mana}".format(**stats))

def player1_turn(stats):
    name1 = input("\n Enter your name,Player 1: ")
    print("Choose your move,", name1,":", end='')
    player_choice1 = input(" Attack,Heal,Cast fireball or Restore mana?")

    if player_choice1 == "Attack":
        damage = random.choice(range(10, 20))
        stats["player2_health"] -= damage
        print("You dealt: ", damage, " damage")
        print_stats(stats)
    elif player_choice1 == "Heal":
        stats["player1_health"] += 10
        print(" Your health now is: ", stats["player1_health"])
        print_stats(stats)
    elif player_choice1 == "Cast fireball":
        stats["player1_mana"] -= 40
        stats["player2_health"] -= 30
        print("Damage dealt: 30")
        print_stats(stats)
    elif player_choice1 == "Restore mana":
        stats["player1_mana"] += 20
        print("You restored 20 mana")
        print_stats(stats)

def main():
    stats = {
        "player1_health" :100,
        "player2_health" :100,
        "player1_mana" :100,
        "player2_mana" :100
    }

    print_game_rules()

    answer = input("\n Let's start?: ")

    answer = answer.lower()

    if answer == "yes":
        print_stats(stats)
    else:
        print("See you later!")
        exit()

    player1_turn(stats)


main()

