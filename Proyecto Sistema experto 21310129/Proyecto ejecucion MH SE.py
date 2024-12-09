import sqlite3

def connect_db():
    conn = sqlite3.connect('monster_hunter.db')
    return conn

def get_monster_info(monster_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Monsters WHERE name = ?", (monster_name,))
    result = cursor.fetchone()
    conn.close()
    return result

def infer_strategy(monster_name, player_weapon):
    monster = get_monster_info(monster_name)
    if not monster:
        return "Monster not found."
    
    name, type_, weakness, resistance = monster[1:]
    if weakness in player_weapon:
        return f"Use your {player_weapon} for an aggressive attack strategy!"
    elif resistance in player_weapon:
        return f"Your {player_weapon} is not effective. Avoid direct combat."
    else:
        return f"Neutral strategy: aim for weak points like the {type_.lower()} core."

# Example Usage
monster_name = "Tigrex"
player_weapon = "Trueno Sword"
print(infer_strategy(monster_name, player_weapon))

