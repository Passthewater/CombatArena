from engine.fighter import Fighter
class Battle:
        def __init__(self, fighter1, fighter2):
            self.fighter1 = fighter1
            self.fighter2 = fighter2
            self.rounds = 0
            self.winner = None
    
        def fight(self):
            while self.fighter1.health > 0 and self.fighter2.health >0:
                self.rounds += 1
                print(f"\n--- Round {self.rounds} ---")
                self.fighter1.attack(self.fighter2)
                if self.fighter2.health > 0:
                    self.fighter2.attack(self.fighter1)
                else:
                    self.winner = self.fighter1
            if not self.winner:
                self.winner = self.fighter2
            if self.winner == self.fighter1 and hasattr(self.fighter2, "xp_reward"):
                self.fighter1.gain_xp(self.fighter2.xp_reward)
            print(f"\n🏆 {self.winner.name} is victorious after {self.rounds} rounds!")