import json
import os
from .config import load_config
def save_player(fighter, path="player_save.json"):
    data = {
        "name": fighter.name,
        "health": fighter.max_health,
        "attack_power": fighter.attack_power,
        "level": fighter.level,
        "xp": fighter.xp
    }
    with open(path, "w") as f:
        json.dump(data, f)

def load_player(path="player_save.json"):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    else:
        print("🔄 No save file found — loading default player.")
        data = load_config("fighters.json")
        return data["player"]