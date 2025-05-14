from engine.fighter import Fighter

class Mage(Fighter):
    def __init__(self, name, health, attack_power, spell_power=20, level=1, xp=0, xp_reward=0):
        super().__init__(name, health, attack_power, spell_power, level, xp, xp_reward)
        self.class_name = "Mage"
        self.mana = 100
        self.max_mana = 100
        self.mana_cost = 10
        self.mana_regen = 5
        self.spell_type = "Fireball"
        self.armour = "Light"

    def take_damage(self, damage, attacker_class_name=None):
        # Apply the actual damage
        super().take_damage(damage)
        # Regenerate mana after taking damage
        self.regenerate_mana()
    
    def attack(self, opponent):
        """Override the base attack method to use spells instead"""
        if self.mana >= self.mana_cost:
            damage = int(self.spell_power * 1.5)  # Mages do 50% more spell damage
            self.mana -= self.mana_cost
            print(f"{self.name} casts {self.spell_type} for {damage} damage!")
            opponent.take_damage(damage, attacker_class_name=self.__class__.__name__)
        else:
            # Fallback to basic attack if out of mana
            damage = self.attack_power
            print(f"{self.name} uses staff attack for {damage} damage!")
            opponent.take_damage(damage, attacker_class_name=self.__class__.__name__)

    def regenerate_mana(self):
        if self.mana < self.max_mana:
            regen_amount = min(
                self.mana_regen + (self.level * 2),
                self.max_mana - self.mana
            )
            self.mana += regen_amount
            print(f"{self.name} regenerates {regen_amount} mana! Current mana: {self.mana}/{self.max_mana}")
