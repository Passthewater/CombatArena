import random
from .utils import critical_hit

class Fighter:
    def __init__(self, name, health, attack_power, spell_power, level=1, xp=0,xp_reward=0, vulnerability = 3):
        self.name = name
        self.health = self.max_health = health
        self.attack_power = attack_power
        self.spell_power = spell_power
        self.min_damage = attack_power // 2 or spell_power // 2
        self.max_damage = attack_power  * 2 or spell_power * 2
        self.level = level
        self.xp = xp
        self.xp_reward = xp_reward
        self.vulnerability = vulnerability

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP! Total XP: {self.xp}")
        if self.xp >= 100:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.attack_power += 2
        self.max_health += 10
        self.health - self.max_health
        print(f"{self.name} leveled up! Now at level {self.level} with {self.max_health} health and {self.attack_power} attack power.")
    
    def roll_attack(self):
        # Simulate a dice roll for attack damage
        damage = random.randint(self.min_damage, self.max_damage)
        return critical_hit(damage, name=self.name)
           
    def attack(self, opponent):
        damage = self.roll_attack()
        opponent.take_damage(damage)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        print(f"{opponent.name} has {opponent.health} health left.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage!")

    def vulnerability (self, damage):
        return int(damage * self.vulnerability)