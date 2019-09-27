import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        attack_strenth = 0
        for ability in range(len(self.abilities)):
            attack_strenth =+ self.abilities[ability].attack()
        return attack_strenth

    def defend(self):
        damage_amt = 0
        for armor in range(len(self.armors)):
            damage_amt =+ self.armors[armor].block()
        return damage_amt

    def take_damage(self, damage):
        attack = damage-self.defend()
        if attack < 0:
            attack = 0 # set attack back to 0 if it goes below 0
        self.current_health = self.current_health-attack

    def is_alive(self):
        if self.current_health <= 0:
            return False
        return True




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(2000)
    print(hero.current_health)
    print(hero.is_alive())
