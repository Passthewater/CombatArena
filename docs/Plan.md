1. __Design the `Item` Structure:__

   - What information does an item need? At a minimum, probably a `name`. Maybe also an `effect` or `value` (e.g., a potion's healing amount, a weapon's damage bonus).
   - For a simple start, we might not even need a full `Item` class yet. We could represent items as dictionaries or simple strings initially and expand later. Let's plan to start simple, perhaps just using strings for item names in the inventory.

2. __Create the `Inventory` Class:__

   - This class will be responsible for managing a collection of items.

   - It will need an attribute to hold the items. A __list__ is a good data structure for this, as it can store multiple items in order and allows for easy adding and removing.

   - It will need methods:

     - `__init__`: To initialize the inventory, likely starting empty.
     - `add_item(item)`: To add an item to the inventory.
     - `remove_item(item)`: To remove an item from the inventory.
     - `list_items()`: To display the items currently in the inventory.
     - Maybe `use_item(item_name, target)`: To handle the logic of using an item (this is more complex and could be a later step).

3. __Integrate `Inventory` into `Fighter` (Composition):__

   - Add an attribute to the `Fighter` class (e.g., `self.inventory`) in its `__init__` method.
   - Initialize this attribute with a new instance of the `Inventory` class: `self.inventory = Inventory()`. Now, every `Fighter` object *has an* `Inventory` object.

4. __Add Initial Items (Optional but helpful):__

   - Modify your `fighters.json` or the `create_fighter` function to allow specifying initial items for a fighter.
   - When creating a fighter, add these initial items to their newly created `self.inventory`.

5. __Basic Inventory Interaction:__

   - Add a method to the `Fighter` class, perhaps `show_inventory()`, that calls the `list_items()` method of its `self.inventory`.
   - Modify the battle loop or add a new interaction point in `main.py` to allow the player to see their inventory.

__TODO for Future Learning (from previous plan + new):__

- __Refine Item Structure:__ Create a dedicated `Item` class with attributes like `name`, `description`, and `effect`.
- __Implement Item Usage:__ Add the `use_item` method to the `Inventory` class and integrate its effects into combat or other game logic.
- __Add Status Effects:__ Create a system for applying and managing status effects (Poison, Stun, etc.) using a data structure and updating effects each round.
- __Expand the Battle System:__ Modify the `Battle` class to handle multiple fighters per side, using lists to manage teams and updating the combat loop.
- __Save/Load Inventory:__ Update the save/load system (`engine/save.py`) to include the fighter's inventory.


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
