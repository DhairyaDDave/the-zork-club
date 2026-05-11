import random

WORLD = {
    "Field": {
        "name": "Open Field",
        "description": "An open green field stretching across the plains, a faded stone path cuts through it.",
        "exits": {
            "north": "Forest", 
            "east": "Village"
        },
        "items": {"female rusty sword" : 1},   # {"item" : [strength, durability]}
        "enemies":{"goomba" : 1}, # {"enemy" : [health, strength]}
        "character":{"female monkey" : 1} # {"character : []"}
    },

    "Forest": {
        "name": "Dark Forest",
        "description": "Tall trees block out most of the light. The air feels heavy.",
        "exits": {
            "south": "Field"
        },
        "items": {},
        "enemies": {"deku kaminari" : 1},
        "character":{""}
    },

    "Village": {
        "name": "Quiet Village",
        "description": "Small cottages line the road. Smoke rises from a few chimneys.",
        "exits": {
            "west": "Field"
        },
        "items": []
    }
}


class Player:
    def __init__(self, health=100, defense=100, currentPos="Field", weapon="Rusty_Sword"):
        self.health = health
        self.defense = defense
        self.currentPos = currentPos
        self.weapon = weapon

    def move(self, direction):
        location = WORLD[self.currentPos]

        if direction in location["exits"]:
            self.currentPos = location["exits"][direction]
            print(f"You move {direction} to {self.currentPos}.")
        else:
            print("You can't go that way.")

    def look(self):
        loc = WORLD[self.currentPos]
        print(f"\n== {loc['name']} ==")
        print(loc["description"])
        print("Exits:", ", ".join(loc["exits"].keys()))

        if loc["character"]:
            print("You see")
            

class GameObject:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Object_Interactive(GameObject):      #work on this later to properly generalise consumables, weapons, 
    def __init__(self, weapons):
        self.weapons = weapons


class Weapon(Object_Interactive):
    def __init__(self, durability, damage_inflicted, status):
        self.durability = durability
        self.damage_inflicted = damage_inflicted
        self.status = status
    
    def set_damage_inflicted(self, damage_inflicted):
        self.damage_inflicted = random(damage_inflicted + 3, damage_inflicted - 3)
    
    def set_status(self, durability, status):
        if durability <= 0:
            self.status = "{self} is broken"
    
"Rusty Sword" = Weapon("Rusty Sword", 20, damage_inflicted=10, status=None)
"Regular Sword" = Weapon("Regular Sword", 50, damage_inflicted=20,status=None)
"Rusty Axe" = Weapon("Rusty Axe", )


class Enemy(GameObject):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage 

    def attack(self, player):
        print(f"The {self.name} attacks you for {self.damage} damage!")
        player.health -= self.damage
        if player.health <= 0:
            print("You have been defeated. Game over.")
            exit()

    def take_damage(self, damage):
        self.health -= damage
        print(f"You hit the {self.name} for {damage} damage!")
        if self.health <= 0:
            print(f"You have defeated the {self.name}!")
 
    def run_away(self):
        print(f"The {self.name} runs away!")
        # Implement logic to remove enemy from current location or move it to a different location


class Location(GameObject):
    def __init__(self, exits, items, characters, currentPos):
        self.exits = {}
        self.items = []
        self.characters = []

        

class NPCs:
    def __init__(self, location, dialogue="none", health="50"):
        self.location = location
        self.dialogue = dialogue
        self.health = health
        
    def talk (self, dialogue):
        print(f"{self.name} says: {self.dialogue}")
        
        if Player = :
            



# GAME LOOPPFUNCTIONS IMPROTNAT

def parse_command(cmd, player):
    words = cmd.lower().split() # splits input into action and description

    if len(words) == 0:
        return

    if words[0] in ["go", "move", "walk"]:
        if len(words) < 2:
            print("Go where")
            return
        direction = words[1]
        player.move(direction)
        return

    if words[0] in ["look", "examine"]:
        player.look()
        return

    # quit
    if words[0] in ["quit", "exit"]:
        print("Goodbye adventurer.")
        return "quit"

    print("I don't understand that command.")
        

def game_loop():
    player = Player()
    print("Welcome to the adventure. You are a women. We are feminists") # Starting Welcome message 
    player.look()

    while True:
        cmd = input("\nWhat do you do: ") # ask nfor input message
        if parse_command(cmd, player) == "quit":
            break
            
# MAIN GAME LOOP

if __name__ == "__main__":
    game_loop()

