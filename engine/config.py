import json
from .classes.knight import Knight
from .classes.mage import Mage
from .fighter import Fighter

def load_config(path):
    with open(path, "r") as f:
        return json.load(f)

def create_fighter(cls, data):
    # Create a copy of data and remove the class key
    fighter_data = data.copy()
    fighter_data.pop('class', None)

    if cls == "Knight":
        # Explicitly pass only the parameters Knight expects
        return Knight(
            name=fighter_data['name'],
            health=fighter_data['health'],
            attack_power=fighter_data['attack_power'],
            level=fighter_data.get('level', 1),
            xp=fighter_data.get('xp', 0),
            xp_reward=fighter_data.get('xp_reward', 0)
        )
    elif cls == "Mage":
        return Mage(
            name=fighter_data['name'],
            health=fighter_data['health'],
            spell_power=fighter_data['spell_power'],
            attack_power=fighter_data['attack_power'],
            level=fighter_data.get('level', 1),
            xp=fighter_data.get('xp', 0),
            xp_reward=fighter_data.get('xp_reward', 0)
        )
    
    return Fighter(**fighter_data)
