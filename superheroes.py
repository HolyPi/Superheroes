import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block
    def block(self):
        random_value = random.randint(0,self.max_block)
        return random_value
class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        strength = random.randint(self.max_damage //2, self.max_damage)
        return strength

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)
    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object'''
        self.armors.append(armor)


    def attack(self):
        '''Calculate the total damage from all ability attacks.'''
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def defend(self):
        '''Calculate the total block amount from all armor blocks.'''
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        self.current_health -= damage - self.defend()

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def is_alive(self):
        '''Determines if heroes are alive'''

        if self.current_health <= 0:
            return False
        else:
            return True

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def fight(self, opponent):

        if self.abilities == [] and opponent.abilities == []:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                hero_attack = self.attack()
                opponent_attack = opponent.attack()
                self.take_damage(opponent_attack)
                opponent.take_damage(hero_attack)
                if self.is_alive() == False:
                    "Determines if opponent wins"
                    print(f'{opponent.name}) won!')
                    self.deaths += 1
                    opponent.kills += 1
                elif opponent.is_alive() == False:
                    "Determines if hero won"
                    print(f'{self.name} won!')
                    self.kills += 1
                    opponent.deaths += 1


class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:

            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)

            random_hero.fight(random_opponent)

            if random_hero.is_alive():
                living_opponents.remove(random_opponent)
            else:
                living_heroes.remove(random_hero)


    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            if hero.deaths == 0:
                kd = hero.kills
            else:
                kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name, kd))

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
                hero.current_health = hero.starting_health



class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = int(input("What is the max damage of the ability?  "))

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is the weapon's name? ")
        max_damage = int(input("What is the max damage of the weapon? "))

        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        name = input("What is the armor's name? ")
        max_block = int(input("What is the max block of the armor? "))

        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               ability = self.create_ability()
               hero.add_ability(ability)
           elif add_item == "2":
               weapon = self.create_weapon()
               hero.add_weapon(weapon)
           elif add_item == "3":
               armor = self.create_armor()
               hero.add_armor(armor)
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        team_name = input("Select your team name for the first team:")
        team_one = Team(team_name)
        num_of_heroes = int(input("Select how many heroes you want on team one:"))
        for heroes_number in range (num_of_heroes):
            hero = self.create_hero()
            team_one.add_hero(hero)
        self.team_one = team_one


    def build_team_two(self):
        '''Prompt the user to build team_two'''
        team_name = input("Select your team name for the second team:")
        team_two = Team(team_name)
        num_of_heroes = int(input("Select how many heroes you want on team two:"))
        for heroes_number in range (num_of_heroes):
            hero  = self.create_hero()
            team_two.add_hero(hero)
            self.team_two = team_two

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        alive_heroes = []
        alive_opponents = []

        for hero in self.team_one.heroes:
            if hero.is_alive():
                alive_heroes.append(hero)

        for hero in self.team_two.heroes:
            if hero.is_alive():
                alive_opponents.append(hero)

        for hero in alive_heroes:
                    print("Heroes that survived.")
                    print(hero.name)

        for hero in alive_opponents:
            print("Enemies that survived.")
            print(hero.name)

        if len(alive_heroes) > len(alive_opponents):
            print(f"Victory goes to {self.team_one.name}")
        elif len(alive_heroes) < len(alive_opponents):
            print(f"Victory goes to {self.team_two.name}")

        else:
            print("It's a draw.")

        print(f'Team one KillDeath ratio: {self.team_one.stats()}')
        print(f'Team two KillDeath ratio: {self.team_two.stats()}')





if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
