from engine import Fighter, Battle
from engine.config import load_config
from engine.save import load_player, save_player
from engine.config import create_fighter

# Main function to run the combat arena

if __name__ == "__main__":
    data = load_config("fighters.json")

    player = create_fighter(data["player"]["class"], data["player"])
    enemy = create_fighter(data["enemy"]["class"], data["enemy"])

    arena = Battle(player, enemy)
    arena.fight()

    save_player(player)