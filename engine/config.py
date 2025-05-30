import json
from .classes.knight import Knight
from .classes.mage import Mage
from .fighter import Fighter
from .items import Item, Inventory

CLASS_MAPPING = {
       "Fighter": Fighter,
       "Knight": Knight,
       "Mage": Mage,
       # Add new classes here as you create them
   }

def load_config(path):
    with open(path, "r") as f:
        return json.load(f)

def create_fighter(cls_name, data,all_items_data):
    fighter_class = CLASS_MAPPING.get(cls_name, None)
    if fighter_class is None:
        raise ValueError(f"Unknown class name: {cls_name}")
    
    fighter_data = data.copy()
    fighter_data.pop("class", None) 

    if fighter_class == Knight:
        new_fighter = Knight(
            name=fighter_data['name'],
            health=fighter_data['health'],
            attack_power=fighter_data['attack_power'],
            level=fighter_data.get('level', 1),
            xp=fighter_data.get('xp', 0),
            xp_reward=fighter_data.get('xp_reward', 0)
        )
    elif fighter_class == Mage:
        new_fighter = Mage(
            name=fighter_data['name'],
            health=fighter_data['health'],
            spell_power=fighter_data['spell_power'],
            attack_power=fighter_data['attack_power'],
            level=fighter_data.get('level', 1),
            xp=fighter_data.get('xp', 0),
            xp_reward=fighter_data.get('xp_reward', 0)
        )
    else:
        new_fighter = fighter_class(**fighter_data)
        
    fighter_item_names = data.get("items", [])
    for item_name in fighter_item_names:
        for item_data in all_items_data:
            if item_data["name"] == item_name:
                item_attr = Item(**item_data)
                new_fighter.inventory.add_item(item_attr)

    return new_fighter


        
