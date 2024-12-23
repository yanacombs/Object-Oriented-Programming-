class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}!, {self.name} deals {target.name} damage, {target.name} now has only {target.health}")
    
    def special_move(self):
        pass
    
    def defend (self, attacker):
        dmg_taken = attacker.power * 0.9
        self.health -= dmg_taken
        print(f"{self.name} defends against {attacker.name}'s attack. {self.name}'s health is now {self.health}.")
        
class Warrior(Character):
    def special_move(self, target):
        self.power *= 2
        print(f"{self.name} uses Shield Bash!")
        
class Mage(Character):
    def special_move(self, target):
        target.health -= 100
        print(f"{self.name} casts Fireball! {target.name}'s health is reduced by 100.")
        
class Archer(Character):
    def special_move(self, target):
        target.health -= self.power * 1.5
        print(f"{self.name} shoots a Piercing Arrow! {target.name}'s health is reduced by 1.5 times than the normal damage.")
        
class Monster(Character):
    def special_move(self, target):
        target.health += 50
        print(f"{self.name} roars and gains 50 health.")
        
judea = Warrior("Judea", 200, 10)
umi = Mage("Umi", 100, 20)
nel = Archer("Nel", 50, 15)
mnstr = Monster("Monster", 150, 20)

characters = [judea, umi, nel]

while True:
    for judea in characters:
        judea.attack(mnstr)
        judea.special_move(mnstr)
        mnstr.defend(judea)

        if mnstr.health <= 0:
            print("Monster defeated!")
    break

    for character in characters:
        monster.attack(character)
        monster.special_move(character)
        character.defend(monster)

    if character.health <= 0:
        print(f"{character.name} is defeated!")
        characters.remove(character)
    break
        
    if not characters:
        print("Monster wins!")
    break
