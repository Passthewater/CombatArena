class Item:
    def __init__(self, name, effect_type=None, effect_value=None, description="", is_equipped=False, is_consumable=False, is_usable=False, equip_slot=None, duration=None):
        self.name = name
        self.description = description
        self.effect_type = effect_type
        self.effect_value = effect_value
        self.is_equipped = is_equipped
        self.is_consumable = is_consumable
        self.is_usable = is_usable
        self.equip_slot = equip_slot
        self.duration = duration
class Inventory:
    def __init__(self):
        self.items = []
        self.equipped_items = {}
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to inventory.")
    
    def remove_item(self, item):
        self.items.remove(item)
        print(f"Removed {item.name} from inventory.")
    
    def list_items(self):
        for item in self.items:
            print(f"- {item.name}: {item.description}")