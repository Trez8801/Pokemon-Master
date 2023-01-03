class Pokemon:
    def __init__(self, name, level, type, maxHealth, curHealth, knocked):
        self.name = name
        self.level = level
        self.type = type
        self.maxHealth = maxHealth
        self.curHealth = curHealth
        self.knocked = knocked
        
    def currentHP(self):
        print(f'{self.name} current HP is {self.curHealth}.')
        
    def attack(self, attack):
        self.curHealth -= attack
        print(f'{self.name} was attacked and now has {self.curHealth} HP.')
        if self.curHealth == 0:
            Pokemon.knockout()
    
    def heal(self, heal):
        if heal + self.curHealth > self.maxHealth:
            dif = self.curHealth - self.maxHealth
            self.curHealth -= dif
            #print(f'You max HP is {self.maxHealth}. You can not heal past this.\n')
            print(f'{self.name} is now back at max health.')
        else:
            self.curHealth += heal
            print(f'{self.name} healed and now has {self.curHealth} HP.')
        
        if self.curHealth == 0:
            Pokemon.revival()
            
    def knockout(self):
        self.knocked = True
        print(f'{self.name} has been knocked out and can no longer be used.')
    
    def revival(self):
        print(f'{self.name} is currently knocked out you must use a revival token. Do you want to?')
        user = input()
        if user == 'Yes':
            self.knocked = False
            self.curHealth += self.maxHealth
            self.revivalToken -= 1
            print(f'{self.name} is fully revived. you have {self.revivalToken} revival tokens left.')
            
    def attack(self, enemy, damage):
        if self.type == 'Fire' and enemy.type == 'Fire':
            attack = damage * .5
            enemy.curHealth -= attack
            print(f'{self.name} has done {attack} damage to {enemy.name}.')
            print(f'{enemy.name} now has {enemy.curHealth} HP.')
        elif self.type == 'Fire' and enemy.type == 'Water':
            attack = damage * .5
            enemy.curHealth -= attack
            print(f'{self.name} has done {attack} damage to {enemy.name}.')
            print(f'{enemy.name} now has {enemy.curHealth} HP.')
        elif self.type == 'Fire' and enemy.type == 'Grass':
            attack = damage * 2
            enemy.curHealth -= attack
            print(f'{self.name} has done {attack} damage to {enemy.name}.')
            print(f'{enemy.name} now has {enemy.curHealth} HP.')
        elif self.type == 'Water' and enemy.type == 'Water':
            attack = damage * .5
            enemy.curHealth -= attack
            print(f'{self.name} has done {attack} damage to {enemy.name}.')
            print(f'{enemy.name} now has {enemy.curHealth} HP.')
        elif self.type == 'Water' and enemy.type == 'Fire':
            attack = damage * 2
            enemy.curHealth -= attack
            print(f'{self.name} has done {attack} damage to {enemy.name}.')
            print(f'{enemy.name} now has {enemy.curHealth} HP.')
        elif self.type == 'Water' and enemy.type == 'Grass':
            attack = damage * .5
            enemy.curHealth -= attack
            print(f'{self.name} has done {attack} damage to {enemy.name}.')
            print(f'{enemy.name} now has {enemy.curHealth} HP.')
        elif self.type == 'Grass' and enemy.type == 'Grass':
            attack = damage * .5
            enemy.curHealth -= attack
            print(f'{self.name} has done {attack} damage to {enemy.name}.')
            print(f'{enemy.name} now has {enemy.curHealth} HP.')
        elif self.type == 'Grass' and enemy.type == 'Water':
            attack = damage * 2
            enemy.curHealth -= attack
            print(f'{self.name} has done {attack} damage to {enemy.name}.')
            print(f'{enemy.name} now has {enemy.curHealth} HP.')
        elif self.type == 'Grass' and enemy.type == 'Fire':
            attack = damage * .5
            enemy.curHealth -= attack       
            print(f'{self.name} has done {attack} damage to {enemy.name}.')
            print(f'{enemy.name} now has {enemy.curHealth} HP.')

class Trainer:
    def __init__(self, name, pokemon, potions, activePokemon):
        self.name = name
        self.pokemon = pokemon
        self.potions = potions
        self.activePokemon = self.pokemon[activePokemon]
    
    def attackTrainer(self, trainer):
        if self.potions != 0:
            self.activePokemon.attack(trainer.activePokemon, 10)
            self.potions -= 1
            print(f'{self.name} has used 1 potion to attack {trainer.name} and now has {self.potions} left.')
        else:
            print(f'{self.name} has no more potions to use.')
            
    def healTrainer(self):
        if self.potions != 0:
            self.activePokemon.heal(10)
            self.potions -= 1
            print(f'{self.name} has used 1 potion to heal and has {self.potions} left.')
        else:
            print(f'{self.name} has no more potions to use.')
            
    def switchActive(self, pokemon): #The pokemon argument takes an index # in order to select the pokemon from the list of pokemons
        self.activePokemon = self.pokemon[pokemon]   
        print(f'{self.name} has switched their active pokemon to {self.activePokemon.name}.') 
    
    def active(self): 
        print(f'Ash\'s  active pokemon is {self.activePokemon.name}')

#Instantiations
Charmander = Pokemon('Charmander', 15, 'Fire', 250, 250, False)
Squirtle = Pokemon('Squirtle', 8, 'Water', 125, 125, False)
Bulbasaur = Pokemon('Bulbasaur', 10, 'Grass', 155, 155, False)

Ash = Trainer('Ash', [Charmander, Squirtle, Bulbasaur], 5, 0)
Trez = Trainer('Trez', [Charmander, Squirtle, Bulbasaur], 5, 1)
