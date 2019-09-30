import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, int(self.max_damage))


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, int(self.max_block))


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
        randomHero = random.randint(0, len(self.heroes))
        randomOpponent = random.randint(0, len(other_team.heroes))
        self.heroes[randomHero-1].fight(other_team.heroes[randomOpponent-1])

    def revive_heroes(self, health=100):
        for hero in self.heroes:
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
            damage_amt = damage_amt + armor.block()
        return damage_amt

    def take_damage(self, damage):
        attack = self.defend()
        attack_val = 0
        if damage - attack > 0:
            attack_val = damage - attack
        else:
            attack_val = 0 # set attack back to 0 if it goes below 0
        self.current_health = int(self.current_health) - int(attack_val)
        # self.current_health -= damage - self.defend()
        # return self.current_health

    def is_alive(self):
        if int(self.current_health) <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if self.is_alive() and not opponent.is_alive():
            self.add_kill(1)
            opponent.add_deaths(1)
            print(self.name, 'won!')
        elif opponent.is_alive() and not self.is_alive():
            opponent.add_kill(1)
            self.add_deaths(1)
            print(opponent.name, 'won!')
        else:
            print('Draw!')


    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

class Arena:
    def __init__(self):
        team_one: list()
        team_two: list()

    def create_ability(self):
        name = input("Enter an ability: ")
        max_damage = input(f"Enter a max damage for {name}: ")
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("Enter a weapon name: ")
        max_damage = input(f"Enter a max damage for {name}: ")
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("Enter an armor name: ")
        max_block = input(f"Enter a max block for {name}: ")
        return Armor(name, max_block)

    def create_hero(self):
        hero = Hero(input("Enter a hero name: "), input("Enter a max health for the hero: "))
        adding = True
        while adding:
            print('ADD ITEMS: ')
            print('1 to add ability\n2 to add a weapon\n3 to add armor\nand 4 to finish\n')
            selection = input()
            if selection == "1":
                hero.add_ability(self.create_ability())
            elif selection == "2":
                hero.add_weapon(self.create_weapon())
            elif selection == "3":
                hero.add_armor(self.create_armor())
            elif selection == "4":
                adding = False
        return hero

    def build_team_one(self):
        team = Team(input("Enter a name for team 1: "))
        heroes_count = int(input("How many heroes would you like for team 1?: "))
        for index in range(heroes_count):
            team.add_hero(self.create_hero())
        self.team_one = team


    def build_team_two(self):
        team = Team(input("Enter a name for team 2: "))
        heroes_count = int(input("How many heroes would you like for team 2?: "))
        for index in range(heroes_count):
            team.add_hero(self.create_hero())
        self.team_two = team

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print('______________________________')
        print('            STATS             ')
        print('______________________________\n')

        alive_in_team_one = []
        num_kills_team_one = 0
        num_deaths_team_one = 0

        alive_in_team_two = []
        num_kills_team_two = 0
        num_deaths_team_two = 0

        for hero in self.team_one.heroes:
            if hero.is_alive():
                alive_in_team_one.append(hero)
            num_kills_team_one += hero.kills
            num_deaths_team_one += hero.deaths

        for hero in self.team_two.heroes:
            if hero.is_alive():
                alive_in_team_two.append(hero)
            num_kills_team_two += hero.kills
            num_deaths_team_two += hero.deaths

        if len(alive_in_team_one) > len(alive_in_team_two):
            print(f'Winner: {self.team_one.name}')
            print(f'with {len(alive_in_team_one)} heroes alive!\n')
            print('Alive heroes (name, kills/deaths):')
            for hero in alive_in_team_one:
                print('{} - {}/{}'.format(hero.name, hero.kills, hero.deaths))
            print(f'\n\nTeam 1 kills/deaths: {num_kills_team_one}')
            print(f'Team 2 kills/deaths: {num_kills_team_two}')

        else:
            print(f'Winner: {self.team_two.name}')
            print(f'with {len(alive_in_team_two)} heroes alive!')


class Weapon(Ability):
    def attack(self):
        return random.randint(int(self.max_damage) // 2, int(self.max_damage))


if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False

        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
