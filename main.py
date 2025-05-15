from engine import Fighter, Battle
from engine.config import load_config
from engine.save import load_player, save_player
from engine.config import create_fighter

# Main function to run the combat arena

if __name__ == "__main__":
    data = load_config("fighters.json")
    player_data = load_player()

    if player_data:
        data["player"].update(player_data)
        print("🔄 Player data loaded from save file.")
    else:
        print("🔄 No save file found — loading default player.")

    player = create_fighter(data["player"]["class"], data["player"])
    player.show_inventory()
    enemy = create_fighter(data["enemy"]["class"], data["enemy"])

    arena = Battle([player], [enemy])
    arena.fight()

    save_player(player)