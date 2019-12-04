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

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

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
    def is_alive(self):
        '''Determines if heroes are alive'''

        if self.current_health <= 0:
            return False
        else:
            return True

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
                    # self.deaths += 1
                    # opponent.kills += 1
                elif opponent.is_alive() == False:
                    "Determines if hero won"
                    print(f'{self.name} won!')
                    # self.kills += 1
                    # opponent.deaths += 1
  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
  # 1) else, start the fighting loop until a hero has won
  # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
  # 3) After each attack, check if either the hero (self) or the opponent is alive
  # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop


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
