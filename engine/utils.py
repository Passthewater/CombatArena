import random
print("🔥 utils.py loaded")

def critical_hit(damage, name=None):
    # Simulate a critical hit
    if random.random() < 0.2:
        print(f"{name} lands a critical hit!")
        return damage * 2
    else:
        return damage
    
def dodge(damage):
    # Simulate a dodge chance
    if random.random() < 0.1:
        print("You dodge the Attack!")
        return 0
    else:
        return damage
    
def block(damage):
    if random.random() < 0.1:
        print("You block the attack!")
        return damage // 2
    else:
        return damage
    
def special_attack():
    # Simulate a special attack chance
    return random.random() < 0.05

def dodge_chance_success(chance):
    return random.random() < chance