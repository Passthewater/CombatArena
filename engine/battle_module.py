from engine.fighter import Fighter
from engine.status_effects import StatusEffect
class Battle:
        def __init__(self, team1, team2):
            self.team1 = team1
            self.team2 = team2
            self.rounds = 0
            self.winner = None
    
        def fight(self):
            while any(fighter.health > 0 for fighter in self.team1) and \
                  any(fighter.health > 0 for fighter in self.team2):
                self.rounds += 1
                print(f"\n--- Round {self.rounds} ---")
                
                for fighter in self.team1:
                    fighter.apply_status_effects()
                    if fighter.has_status_effect("stun"):
                        continue
                    fighter.manage_self()
                    if fighter.health > 0:
                        target = None
                        for opponent in self.team2:
                            if opponent.health > 0:
                                target = opponent
                                break

                        if target is not None:
                            fighter.attack(target)
                        
                        if not any(fighter.health > 0 for fighter in self.team2):
                            self.winner = self.team1
                            self.distribute_xp()
                            break
                    
                for fighter in self.team2:
                    fighter.apply_status_effects()
                    if fighter.has_status_effect("stun"):
                        continue
                    fighter.manage_self()
                    if fighter.health > 0:
                        target = None
                        for opponent in self.team1:
                            if opponent.health > 0:
                                target = opponent
                                break
                        
                        if target is not None:
                            fighter.attack(target)
                        
                        if not any(fighter.health > 0 for fighter in self.team1):
                            self.winner = self.team2
                            self.distribute_xp()
                            break
        def distribute_xp(self):
            total_xp_gained = 0
            if self.winner == self.team1:
                for fighter in self.team2:
                    if fighter.health <= 0:
                        total_xp_gained += fighter.xp_reward
                for fighter in self.team1:
                    if fighter.health > 0:
                        fighter.gain_xp(total_xp_gained)
            elif self.winner == self.team2:
                for fighter in self.team1:
                    if fighter.health <= 0:
                        total_xp_gained += fighter.xp_reward
                for fighter in self.team2:
                    if fighter.health > 0:
                        fighter.gain_xp(total_xp_gained)
                    

                
