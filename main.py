

WORLD = {
    "Field": {
        "name": "Open Field",
        "description": "An open green field stretching across the plains, a faded stone path cuts through it.",
        "exits": {
            "north": "Forest",
            "east": "Village"
        },
        "items": []
    },

    "Forest": {
        "name": "Dark Forest",
        "description": "Tall trees block out most of the light. The air feels heavy.",
        "exits": {
            "south": "Field"
        },
        "items": []
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
    def __init__(self, health=100, defense=100, currentPos="Field", weapon=None):
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


def parse_command(cmd, player):
    words = cmd.lower().split()

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



        
    
class GameObject:
    def __init__(self, name, description):
        self.name = name
        self. description = description


class Object_Interactive(GameObject):      #work on this later to properly generalise consumables, weapons, 
    def __init__(self, hurt):
        self.hurt = hurt


#this class is temporary

class Weapon:
    def __init__(self, durability, damage_inflected, status):
        self.durability = durability
        self.damage_inflected = damage_inflected
        self.status = status


class Location(GameObject):
    def __init__(self, exits, items, characters, currentPos):
        self.exits = {}
        self.items = []
        self.characters = []

        

class NPCs:
    def __init__(self, name):
        self.name = name



def game_loop():
    player = Player()
    print("Welcome to the adventure.")
    player.look()

    while True:
        cmd = input("\nWhat do you do: ")
        if parse_command(cmd, player) == "quit":
            break


if __name__ == "__main__":
    game_loop()