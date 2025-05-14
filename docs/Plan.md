Here is a plan to refactor the `create_fighter` function in `engine/config.py`:

__Plan: Refactoring Fighter Creation__

__Goal:__ Replace the `if/elif` chain in `create_fighter` with a more flexible approach using a dictionary lookup.

__Steps:__

1. __Understand the Problem:__ The current `create_fighter` function relies on a series of `if/elif` statements to check the `class` string from the configuration data and then manually instantiate the correct class (`Knight`, `Mage`, or `Fighter`). This works for a few classes, but adding a new class requires adding a new `elif` block, which makes the function grow and become harder to maintain.

2. __Introduce a Class Mapping Dictionary:__ We will create a dictionary within `engine/config.py` that maps the string names of the classes (like `"Knight"`, `"Mage"`, `"Fighter"`) to the actual Python class objects (`Knight`, `Mage`, `Fighter`). This dictionary will serve as a lookup table.

   ```python
   # Inside engine/config.py, after imports
   CLASS_MAPPING = {
       "Fighter": Fighter,
       "Knight": Knight,
       "Mage": Mage,
       # Add new classes here as you create them
   }
   ```

3. __Modify `create_fighter` to Use the Mapping:__

   - The function will take the `cls` string (e.g., `"Knight"`) and use it as a key to look up the corresponding class object in the `CLASS_MAPPING` dictionary.
   - Once the class object is retrieved, we will instantiate it.

4. __Handle Different `__init__` Signatures:__

   - The `Fighter`, `Knight`, and `Mage` classes have slightly different parameters in their `__init__` methods. The current `if/elif` explicitly passes the required parameters for each class.
   - We need to maintain this behavior. After looking up the class object in the `CLASS_MAPPING`, we will check which class it is and pass the appropriate arguments from the `fighter_data` dictionary. This still involves a check, but it's based on the class object itself, which is generally preferred over string comparisons for type checking.

__Refactored `create_fighter` (Conceptual):__

```python
# Inside engine/config.py

# ... imports and CLASS_MAPPING dictionary ...

def create_fighter(cls_name, data):
    # Get the class object from the mapping
    fighter_class = CLASS_MAPPING.get(cls_name)

    if fighter_class is None:
        print(f"Error: Unknown fighter class '{cls_name}'")
        return None # Or raise an error

    # Create a copy of data and remove the class key
    fighter_data = data.copy()
    fighter_data.pop('class', None)

    # Instantiate the correct class with appropriate arguments
    if fighter_class == Knight:
         return Knight(
            name=fighter_data['name'],
            health=fighter_data['health'],
            attack_power=fighter_data['attack_power'],
            level=fighter_data.get('level', 1),
            xp=fighter_data.get('xp', 0),
            xp_reward=fighter_data.get('xp_reward', 0)
        )
    elif fighter_class == Mage:
        return Mage(
            name=fighter_data['name'],
            health=fighter_data['health'],
            spell_power=fighter_data['spell_power'],
            attack_power=fighter_data['attack_power'],
            level=fighter_data.get('level', 1),
            xp=fighter_data.get('xp', 0),
            xp_reward=fighter_data.get('xp_reward', 0)
        )
    else: # Assume it's the base Fighter or another class that accepts **kwargs
        return fighter_class(**fighter_data)
```

*(Note: The base `Fighter` class's `__init__` currently expects `spell_power` as a positional argument. Using `**fighter_data` might require adjusting the `Fighter.__init__` signature to accept `**kwargs` or ensuring `spell_power` is always present in the data, even if 0, for non-Mages. We can address this when implementing.)*

__TODO for Future Learning:__

- __Implement an Inventory System:__ Design and add an `Inventory` class using a list or dictionary. Integrate it into the `Fighter` class using composition.
- __Add Status Effects:__ Create a system for applying and managing status effects (Poison, Stun, etc.) using a data structure and updating effects each round.
- __Expand the Battle System:__ Modify the `Battle` class to handle multiple fighters per side, using lists to manage teams and updating the combat loop.

This plan focuses on the refactoring of `create_fighter` first, as it's a good, contained task that uses dictionaries effectively.


- __Refactoring Fighter Creation (`engine/config.py`):__

  - Currently, the `create_fighter` function uses an `if/elif` chain to determine which class to instantiate based on the `"class"` string in your `fighters.json`. As you add more classes (Archer, Rogue, etc.), this function will get longer and harder to manage.
  - __Learning Opportunity:__ We could refactor this using a dictionary to map class names to class objects. This is a simple form of the __Factory Pattern__ and makes adding new classes much cleaner. It reinforces using __dictionaries__ effectively.

- __Implementing an Inventory System:__

  - Fighters could have items (potions, weapons, armor) that affect their stats or provide abilities.
  - __Learning Opportunity:__ This would involve creating an `Inventory` class that uses a __data structure__ (like a list or dictionary) to hold items. You'd need methods to add, remove, and use items. This introduces the concept of __object composition__ (a Fighter *has* an Inventory).

- __Adding Status Effects:__

  - Introduce effects like Poison (damage over time), Stun (skip turn), or buffs/debuffs (temporary stat changes).
  - __Learning Opportunity:__ You could use a __data structure__ (like a dictionary or list) within the `Fighter` class to track active effects. Applying these effects each round would involve __algorithms__ to iterate through the active effects, apply their logic, and manage their duration.

- __Expanding the Battle System (`engine/battle_module.py`):__

  - Right now, it's a 1v1 battle. You could expand this to handle multiple fighters on each side (a party system).
  - __Learning Opportunity:__ This would require changing the `Battle` class to manage __lists__ of `Fighter` objects and modifying the combat loop to iterate through these lists, deciding who attacks whom (potentially introducing simple __AI logic__ or targeting rules).
