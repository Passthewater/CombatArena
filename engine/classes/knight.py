from engine.fighter import Fighter
from engine.utils import block, dodge, dodge_chance_success

class Knight(Fighter):
    def __init__(self, name, health, attack_power, level=1, xp=0, xp_reward=0):
        # Pass parameters in the order expected by Fighter.__init__
        # Provide a default value for spell_power as Knight doesn't use it directly
        super().__init__(name, health, attack_power, 0, level, xp, xp_reward)
        self.class_name = "Knight"
        self.block_chance = 0.3
        self.dodge_chance = 0.05
        self.magic_vulnerability = 1.5
        self.armour = "Heavy"
    
    def take_damage(self, damage, attacker_class_name=None):
        if attacker_class_name == "Mage":
            damage = super().vulnerability(damage)
        
        if self.block_chance > 0 and dodge_chance_success(self.block_chance):
            print(f"{self.name} blocks the attack!")
            damage = block(damage)
        elif self.dodge_chance > 0 and dodge_chance_success(self.dodge_chance):
            print(f"{self.name} dodges the attack!")
            damage = dodge(damage)
        super().take_damage(damage)
