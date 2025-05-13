# 🛡️ Combat Arena: Rise of the Mighty

<p align="center">
  <img src="resources/the_mighty_logo.png" alt="The Mighty Logo" width="400"/>
</p>

Welcome to **Combat Arena**, a modular, text-based Python battle simulator where *critical hits*, *level-ups*, and *goblin guts* are just part of the journey.

⚔️ **Fight. Level. Save. Repeat.**

---

## 💾 Features

- 🎲 Dice-based combat system with critical hits
- 💥 Modular architecture (Fighter, Battle, Utils, Save, Config)
- 🧠 Dynamic XP system with auto-scaling levels and stats
- 💾 Save/load functionality with JSON persistence
- 🧪 Expandable with loot, enemy classes, and world maps
- 🛠️ Fully structured with clean file imports and utility modules

---

## 📂 Project Structure
combat_arena/
│
├── engine/
│ ├── init.py
│ ├── fighter.py
│ ├── battle.py
│ ├── config.py
│ ├── save.py
│ └── utils.py
│
├── fighters.json
├── player_save.json
└── main.py


---

## 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/combat-arena.git
   cd combat-arena

2. Run the game
    python main.py

3. Modify fighters.json to add new enemies, or upgrade the Mighty 🔥

📖 How It Works
The player and enemies are loaded from JSON files

Combat runs turn-based in the terminal

Critical hits are RNG-based and double the damage

XP is rewarded per kill, triggering level-ups when thresholds are hit

Player state is saved between sessions

🧙‍♂️ Future Plans
☑️ Multi-enemy gauntlet battles

⬜️ Loot drops and equipment

⬜️ Shop system

⬜️ Boss fights with custom AI

⬜️ CLI interface with commands

🧼 License
MIT. Do what you want. Just give Matt the Mighty his due credit.
