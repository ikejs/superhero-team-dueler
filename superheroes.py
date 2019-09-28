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

    def attack(self, other_team):
        randomHero = random.randint(0, len(self.heroes)-1)
        randomOpponent = random.randint(0, len(other_team.heroes)-1)
        self.heroes[randomHero].fight(other_team.heroes[randomOpponent])

    def revive_heroes(self, health=100):
        for heroes in self.heroes:
            hero.starting_health = health
        pass


    def stats(self):
        for member in self.heroes:
            print(f'{member.name}: {member.kills}/{member.deaths}')

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

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
            self.add_kill(1)
            opponent.add_deaths(1)
            print(self.name, 'won!')
        elif len(opponent.abilities)>=0 and len(self.abilities)>=1:
            opponent.add_kill(1)
            self.add_deaths(1)
            print(opponent.name, 'won!')
        else:
            print('Draw!')


    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths


class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    team1 = Team("Team One")
    team2 = Team("Team Two")
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    team1.add_hero(hero1)
    team2.add_hero(hero2)
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
    team1.stats()
    team2.stats()
