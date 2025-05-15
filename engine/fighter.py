import random
from .utils import critical_hit
from .items import Item, Inventory
from .status_effects import StatusEffect

class Fighter:
    def __init__(self, name, health, attack_power, spell_power, level=1, xp=0, xp_reward=0, vulnerability_multiplier=3):
        self.name = name
        self.health = self.max_health = health
        self.attack_power = attack_power
        self.spell_power = spell_power
        self.min_damage = attack_power // 2 or spell_power // 2
        self.max_damage = attack_power  * 2 or spell_power * 2
        self.level = level
        self.xp = xp
        self.xp_reward = xp_reward
        self.vulnerability_multiplier = vulnerability_multiplier
        self.inventory = Inventory()
        self.status_effects = {}


    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP! Total XP: {self.xp}")
        if self.xp >= 100:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.attack_power += 2
        self.max_health += 10
        self.health = self.max_health
        print(f"{self.name} leveled up! Now at level {self.level} with {self.max_health} health and {self.attack_power} attack power.")
    
    def roll_attack(self):
        # Simulate a dice roll for attack damage
        damage = random.randint(self.min_damage, self.max_damage)
        return critical_hit(damage, name=self.name)
           
    def attack(self, opponent):
        damage = self.roll_attack()
        opponent.take_damage(damage, attacker_class_name=self.__class__.__name__)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        print(f"{opponent.name} has {opponent.health} health left.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage!")

    def vulnerability(self, damage):
        return int(damage * self.vulnerability_multiplier)
    
    def show_inventory(self):
        print(f"{self.name}'s Inventory:")
        self.inventory.list_items()

    def has_status_effect(self, effect_name):
        for effect in self.status_effects:
            if effect.name == effect_name:
                return True
        return False
    
    def heal(self, healing_amount):
        self.health += healing_amount
        self.health = min(self.max_health, self.health)
        print(f"{self.name} heals for {healing_amount} health!")
    
    def add_status_effect(self, effect):
        if effect.name in self.status_effects:
            self.status_effects[effect.name].duration += effect.duration
        else:
            self.status_effects[effect.name] = effect
        print(f"{self.name} is affected by {effect.name} for {effect.duration} turns.")

    def apply_status_effects(self):
        effects_to_remove = [] 

    
        for effect in self.status_effects.values():
            if effect.effect_type == "heal":
                self.heal(effect.value)
            elif effect.effect_type == "poison":
                self.take_damage(effect.value)
            elif effect.effect_type == "stun":
                print(f"{self.name} is stunned and cannot attack this turn!")
        # Add other effect types here later

            effect.duration -= 1

            if effect.duration <= 0:
                effects_to_remove.append(effect.name) 

    
        for effect_name in effects_to_remove:
       
            if effect_name in self.status_effects:
                del self.status_effects[effect_name]
                print(f"{self.name}'s {effect_name} effect has worn off.")

    def use_item(self, item):
        print(f"Attempting to use {item.name}...")
        if item.is_useable and item.duration is not None:
            new_effect = StatusEffect(item.name,item.effect_type, item.duration, item.effect_value)
            print(f"{self.name} uses {item.name}!")
            self.add_status_effect(new_effect)
            if item.is_consumable:
                self.inventory.remove_item(item)
                print(f"{item.name} has been consumed.")
        
        else:
            print(f"{item.name} cannot be used.")