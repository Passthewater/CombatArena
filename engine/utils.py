import random
print("🔥 utils.py loaded")

def critical_hit(damage, name=None):
    # Simulate a critical hit
    if random.random() < 0.2:
        print(f"{name} lands a critical hit!")
        return damage * 2
    else:
        return damage