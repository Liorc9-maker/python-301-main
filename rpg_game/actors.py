import random

class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Hero {self.name} (Level {self.level})"

class Opponent:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Digital Opponent: {self.name} at Level {self.level}"

    def attack(self, hero):
        print(f"{hero.name} attacks {self.name}!")

        hero_roll = random.randint(1, 12) * hero.level
        opp_roll = random.randint(1, 12) * self.level

        print(f"You roll {hero_roll}...")
        print(f"The {self.name} rolls {opp_roll}...")

        if hero_roll >= opp_roll:
            print(f"{hero.name} has remained victorious over {self.name}!\n")
            hero.level += self.level
            return True
        else:
            print(f"DEFEAT! {self.name} has overpowered {hero.name}!\n")
            return False

class SmallOpponent(Opponent):
    def __init__(self, name, level, is_buggy=False):
        super().__init__(name, level)
        self.is_buggy = is_buggy
    
    def attack(self, hero):
        print(f"{hero.name} attacks the small opponent {self.name}!")

        hero_roll = random.randint(1, 12) * hero.level
        opp_roll = random.randint(2, 12) * self.level

        print(f"You roll {hero_roll}...")
        print(f"The {self.name} rolls {opp_roll}...")

        if hero_roll >= opp_roll:
            print(f"{hero.name} has defeated {self.name}!\n")
            hero.level += self.level + 5
            return True
        else:
            print(f"DEFEAT! {self.name} has overpowered {hero.name}!\n")
            return False

class FinalBoss(Opponent):
    def attack(self, hero):
        print(f"{hero.name} attacks the FINAL BOSS: {self.name}!")

        hero_roll = random.randint(4, 12) * hero.level
        opp_roll = random.randint(1, 8) * self.level

        print(f"You roll {hero_roll}...")
        print(f"The {self.name} rolls {opp_roll}...")

        if hero_roll >= opp_roll:
            print(f"{hero.name} has defeated the Final Boss {self.name}!\n")
            return True
        else:
            print(f"DEFEAT! {self.name} has overpowered {hero.name}!\n")
            return False
