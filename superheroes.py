import random

class Ability:
    def __init__(self, name, max_damage):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      random_value = random.randint(0,self.max_damage)
      return random_value

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
        defense = self.defend()
        self.current_health -= damage - defense

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

            if random_hero.is_alive() and random_opponent.is_alive == False:
                living_opponents.remove(random_opponent)
            else:
                if random_opponent.is_alive() and random_hero.is_alive == False:
                    living_heroes.remove(random_hero)



    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
                hero.current_health = hero.starting_health



class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.



if __name__ == "__main__":

    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pan", 90)
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    # armor = Armor("Debugging Shield", 10)
    # print(armor.name)
    # print(armor.block())
    # my_hero.add_ability(ability)
    # print(my_hero.abilities)


    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
