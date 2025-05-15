__Plan:__

1. __Modify `Battle` Initialization:__

   - Change the `__init__` method of the `Battle` class in `engine/battle_module.py`.
   - Instead of taking `fighter1` and `fighter2` as arguments, it should accept two lists of `Fighter` objects, perhaps named `team1` and `team2`.
   - Store these lists as attributes, e.g., `self.team1` and `self.team2`.
   - Keep `self.rounds` and `self.winner` (though `self.winner` might represent the winning *team* or be determined by checking if one team is empty).

2. __Update the `fight` Method Logic:__

   - The `while` loop condition needs to change. Instead of checking the health of two specific fighters, it should continue as long as *both* teams have at least one fighter with health greater than 0.

   - Inside the loop, we need to iterate through the fighters on each team to give them a turn. A simple approach is to have all living fighters on `team1` take a turn, then all living fighters on `team2` take a turn.

   - For each fighter's turn:

     - Check if the fighter's health is greater than 0. If not, they are defeated and skip their turn.
     - If the fighter is alive, they need to choose a target from the * opposing* team.
     - __Simple AI for Target Selection:__ For a start, the fighter can simply target the first living fighter in the opposing team's list, or a random living fighter from the opposing team. We can refine this later.
     - Call the attacking fighter's `attack()` method, passing the chosen target fighter as the argument.
     - After an attack, check if the target fighter's health has dropped to 0 or below. If so, they are defeated. You might want to remove defeated fighters from their team's list or mark them as inactive.
__Areas for potential future improvement (not required for this step, but good to think about):__

- __Target Selection AI:__ The current target selection is very simple (always the first living opponent). As you develop your game, you might want to implement more sophisticated AI, such as targeting the opponent with the lowest health, a random opponent, or prioritizing certain types of opponents.
- __Handling Simultaneous Defeat:__ While unlikely with turn-based combat, in some game systems, it's possible for both teams to be defeated in the same "round" (e.g., if a status effect damages all fighters at the start of a round). Your current logic checks after each team's turn, which is generally sufficient for turn-based, but it's something to consider in more complex scenarios.
- __Code Repetition:__ You have very similar blocks of code for Team 1's turns and Team 2's turns. While this is clear for now, in larger projects, you might consider if there's a way to reduce this repetition, perhaps by creating a helper method for a team's turn or using a loop to iterate through the teams themselves. For learning purposes, repeating the code is fine as it helps solidify the logic.

3. __Determine Battle End and Winner:__

   - After each round (or after each team has taken its turns), check if either `self.team1` or `self.team2` is empty (or contains no living fighters).
   - If `self.team2` is empty, `self.team1` wins.
   - If `self.team1` is empty, `self.team2` wins.
   - Set `self.winner` accordingly and break the `while` loop.
   - Handle XP distribution to the winning team's fighters if applicable (this will need to be updated to distribute XP from all defeated opponents).

4. __Refine Fighter Defeat:__

   - When a fighter's health drops to 0 or below, they should be considered defeated. You might add a `is_defeated` attribute to the `Fighter` class or simply check `fighter.health <= 0`.
   - Update the battle loop to skip turns for defeated fighters and to determine the end of the battle based on whether all fighters on a team are defeated.
