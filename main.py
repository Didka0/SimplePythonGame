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
    print("Choose your move,", stats["player1_name"] ,":", end='')
    player_choice1 = input(" Attack,Heal,Cast fireball or Restore mana?")
    player_choice1 = player_choice1.lower()

    if player_choice1 == "attack":
        damage = random.choice(range(10, 20))
        stats["player2_health"] -= damage
        print("You dealt: ", damage, " damage")
        print_stats(stats)
    elif player_choice1 == "heal":
        stats["player1_health"] += 10
        print(" Your health now is: ", stats["player1_health"])
        print_stats(stats)
    elif player_choice1 == "cast fireball":
        stats["player1_mana"] -= 40
        stats["player2_health"] -= 30
        print("Damage dealt: 30")
        print_stats(stats)
    elif player_choice1 == "restore mana":
        stats["player1_mana"] += 20
        print("You restored 20 mana")
        print_stats(stats)

def player2_turn(stats):
    print("Choose your move,", stats["player2_name"], ":", end='')
    player_choice2 = input(" Attack,Heal,Cast fireball or Restore mana?")
    player_choice2 = player_choice2.lower()
    if player_choice2 == "attack":
        damage = random.choice(range(10, 20))
        stats["player1_health"] -= damage
        print("You dealt: ", damage, " damage")
        print_stats(stats)
    elif player_choice2 == "heal":
        stats["player2_health"] += 10
        print(" Your health now is: ", stats["player2_health"])
        print_stats(stats)
    elif player_choice2 == "cast fireball":
        stats["player2_mana"] -= 40
        stats["player1_health"] -= 30
        print("Damage dealt: 30")
        print_stats(stats)
    elif player_choice2 == "restore mana":
        stats["player2_mana"] += 20
        print("You restored 20 mana")
        print_stats(stats)


def main():
    stats = {
        "player1_health" :100,
        "player2_health" :100,
        "player1_mana" :100,
        "player2_mana" :100,
        "player1_name": None,
        "player2_name": None
    }

    print_game_rules()

    answer = input("\n Let's start?: ")

    answer = answer.lower()

    if answer == "yes":
        print_stats(stats)
    else:
        print("See you later!")
        exit()

    stats["player1_name"] = input("\n Enter your name,Player 1: ").capitalize()
    stats["player2_name"] = input("\n Enter your name,Player 2: ").capitalize()
    
    while (True):
        player1_turn(stats)

        if stats["player2_health"] <= 0:
            print("Player 1 wins")
            break

        player2_turn(stats)

        if stats["player1_health"] <= 0:
            print("Player 2 wins")
            break


main()

