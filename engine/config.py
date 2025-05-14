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
    
    # Remove spell_power for Knight class
    if cls == "Knight":
        fighter_data.pop('spell_power', None)
        return Knight(**fighter_data)
    elif cls == "Mage":
        return Mage(**fighter_data)
    
    return Fighter(**fighter_data)