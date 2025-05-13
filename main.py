from engine import Fighter, Battle
from engine.config import load_config
from engine.save import load_player, save_player

# Main function to run the combat arena

if __name__ == "__main__":
    player_data = load_player()
    player = Fighter(**player_data)

    enemy_data = load_config("fighters.json")["enemy"]
    enemy = Fighter(**enemy_data)

    arena = Battle(player, enemy)
    arena.fight()

    save_player(player)