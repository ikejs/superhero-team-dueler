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


class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours".format(
                self.name,
                self.sleep_duration
            )
        )

class Dog(Animal):
    def bark(self):
        print("Woof Woof!")

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

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
        attack_strength = 0
        for ability in self.abilities:
            attack_strength = attack_strength + ability.attack()
        return attack_strength

    def defend(self):
        damage_amt = 0
        for armor in self.armors:
            damage_amt = damage_amt + armor.attack()
        return damage_amt

    def take_damage(self, damage):
        attack = self.defend()
        # print(type(attack))
        # print(type(damage))

        attack_val = 0
        if damage - attack > 0:
            attack_val = damage - attack
        else:
            attack_val = 0 # set attack back to 0 if it goes below 0
        self.current_health = self.current_health - attack_val
        # self.current_health -= damage - self.defend()
        # return self.current_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if len(self.abilities)>=0 and len(opponent.abilities)>=1:
            print(self.name, 'won!')
        elif len(opponent.abilities)>=0 and len(self.abilities)>=1:
            print(opponent.name, 'won!')
        else:
            print('Draw!')


class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    my_dog = Dog("Sophie", 12)
    my_dog.sleep()
    my_dog.bark()
