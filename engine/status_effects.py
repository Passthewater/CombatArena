from fighter import Fighter
class StatusEffect:
    def __init__(self, name, duration, value, effect_type):
        self.name =  name
        self.duration = duration
        self.value = value
        self.effect_type = effect_type
        

    def effect(self, target_fighter):
        if self.effect_type == "heal":
            target_fighter.heal(self.value)
        elif self.effect_type == "poison":
            target_fighter.take_damage(self.value)
        elif self.effect_type == "stun":
            target_fighter.stun(self.value)



    def time(self):
        pass