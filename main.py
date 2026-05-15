import random

WORLD = {
    "Field": {
        "name": "Open Field",
        "description": "An open green field stretching across the plains, a faded stone path cuts through it.",
        "exits": {
            "north": "Forest",
            "east": "Village"
        },
        "items": {"female rusty sword": 1},
        "enemies": {"female goomba": 1},
        "character": {"female monkey": 1}
    },

    "Forest": {
        "name": "Dark Forest",
        "description": "Tall trees block out most of the light. The air feels heavy.",
        "exits": {
            "south": "Field"
        },
        "items": {},
        "enemies": {"deku kaminari": 1},
        "character": {"monkey soldier"}   # FIXED: cannot be {" "}
    },

    "Village": {
        "name": "Quiet Village",
        "description": "Small cottages line the road. Smoke rises from a few chimneys.",
        "exits": {
            "west": "Field"
        },
        "items": {},   # FIXED: must be dict, not list
        "character": {"villager": 1}
    }
}


class Player:
    def __init__(self, health=100, defense=100, currentPos="Field", weapon="Rusty Sword"):
        self.health = health
        self.defense = defense
        self.currentPos = currentPos
        self.weapon = weapon

    def move(self, direction):
        location = WORLD[self.currentPos]

        if direction in location["exits"]:
            self.currentPos = location["exits"][direction]
            print(f"\nYou move {direction}.")

        # SHOW ROOM FIRST
        self.look()

        #THEN CHECK FOR ENEMIES
        current_location = WORLD[self.currentPos]

        if current_location["enemies"]:
            enemy = current_location["enemies"][0]

            print(f"\nA {enemy.name} appears!")
            combat(self, enemy)

        else:
            print("You can't go that way.")

    def look(self):
        loc = WORLD[self.currentPos]
        print(f"\n== {loc['name']} ==")
        print(loc["description"])
        print("Exits:", ", ".join(loc["exits"].keys()))

        if loc.get("character"):
            print("You see:", ", ".join(loc["character"].keys()))
            for npc in loc["character"]:
                print(f" - {npc.name}")


class GameObject:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Object_Interactive(GameObject):
    def __init__(self, name, description):
        super().__init__(name, description)


class Consumables(Object_Interactive):
    def __init__(self, name, description):
        super().__init__(name, f"A {name}")


class Weapon(Object_Interactive):
    def __init__(self, name, durability, damage_inflicted, status=None):
        super().__init__(name, f"A {name}")
        self.durability = durability
        self.damage_inflicted = damage_inflicted
        self.status = status

    def set_damage_inflicted(self):
        self.damage_inflicted = random.randint(self.damage_inflicted - 3, self.damage_inflicted + 3)

    def set_status(self):
        if self.durability <= 0:
            self.status = f"{self.name} is broken"

Rusty_Sword = Weapon("Rusty Sword", 20, 10)
Regular_Sword = Weapon("Regular Sword", 50, 20)
Rusty_Axe = Weapon("Rusty Axe", 15, 12)


class Enemy(GameObject):
    def __init__(self, name, health, damage):
        super().__init__(name, f"A dangerous {name}")
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


class NPC:
    def __init__(self, name, location, dialogue="none", health=50, hostile=True):
        self.name = name
        self.dialogue = dialogue
        self.health = health
        self.hostile = hostile

    def talk(self):
        print(f"{self.name} says: {self.dialogue}")

    def attack(self, player):
        if not self.hostile :
            print(f"{self.name} doesn't seem interested in throwing hands.")
            return

        damage = 10
        player.health -= damage
        print(f"{self.name} attacks you for {damage} damage!!! Your health is now {player.health}.")
        if player.health <= 8:
            print("You have been defeated...rip")

    def take_damage(self, amount, player):
        self.health -= amount
        print(f"You hit {self.name} for {amount} damage!!! Their health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been murked!!!")
            
            for  loc in World.values():
                if self in loc["character"]:
                    loc["character"].remove(self)
                    break
        else:
            if self.hostile:
                self.attack_player(player)

# GAME LOOP FUNCTIONS

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
    
    if words[0] in ["talk", "speak"]:
        words[1].talk()
        

    if words[0] in ["quit", "exit"]:
        print("Goodbye adventurer.")
        return "quit"

    print("I don't understand that command.")


def game_loop():
    player = Player()
    print("Welcome to the adventure. You are a woman. We are feminists")
    player.look()

    while True:
        cmd = input("\nWhat do you do: ")
        if parse_command(cmd, player) == "quit":
            break


if __name__ == "__main__":
    game_loop()
 