import time
import random
from actors import Hero, Opponent, SmallOpponent, FinalBoss

def main():
    print_welcome()
    play_game()

def print_welcome():
    print("""
----------------------------------------------------------
----------- Welcome to the Legend of Link RPG! -----------
----------------------------------------------------------

A dark shadow was cast over the lands of Heirulez. You are
the chosen one who shall venture through the forests of
the web to defeat what lurks a few links off Google's main
results. The wwworld needs you to restore peaceful linking
to the internet...

""")

def play_game():
    opponents = [
        SmallOpponent('.docx', 1, is_buggy=True),
        SmallOpponent('FTP-Server', 5, is_buggy=False),
        SmallOpponent('www.xxx.com', 10,is_buggy=True ),
        SmallOpponent('.php', 15, is_buggy=False),
        Opponent('Pop-up Ad', 20),
        Opponent('Paywall', 30),
        Opponent('Wordpress-Site', 50),
        FinalBoss('Google Data Center', 500),
    ]

    hero = Hero('Link', 42)

    while True:
        if not opponents:
            print("\n🎉 Congratulations! You've restored peaceful linking to the internet.")
            print("The web is once again safe thanks to you!")
            break

        current_opponent = random.choice(opponents)
        print(f"101010111beeeep... A wild {current_opponent.name} \
at Level {current_opponent.level} has appeared.\n")
         
        if isinstance(current_opponent, SmallOpponent) and current_opponent.is_buggy:
            print(f"The {current_opponent.name} seems buggy... Maybe it'll crash on its own?")


        cmd = input("Do you want to [a]ttack, [r]unaway, or [l]ook around? ")

        while cmd not in ['a', 'r', 'l', 'q']:
            print("Please enter one of the three letters [a, r, l] to play")
            print("To exit game, type [q] for 'quit'.")
            cmd = input("Do you want to [a]ttack, [r]unaway, or [l]ook around? ")

        if cmd == 'a':
            if current_opponent.attack(hero):
                opponents.remove(current_opponent)
            else:
                print(f"{hero.name} caps their internet connection in despair...")
                time.sleep(5)
                print(f"{hero.name} comes back online refreshed!\n")

        elif cmd == 'r':
            print("You got away safely...\n")

        elif cmd == 'l':
            print(f"Hacking and checking out the surroundings... |Oh!| {hero.name} sees:")
            for op in opponents:
                print(f"* A {op.name} of Level {op.level}")
            print()

        elif cmd == 'q':
            print("\nExiting LINK RPG. ByeBye...")
            break

if __name__ == '__main__':
    main()
