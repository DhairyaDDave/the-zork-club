import 


WORLD = {
    "Field" : {
        "name" : "Open Field" ,
        "description" : "An open green field stretching across the plains, a faded stone path cuts through it" ,
        "exits" : {"north", ""} ,
        "items" : []
    }


}


class Player:
    def __init__(self, health, defense, curentPos, weapon, ):
        self.health = 100
        self.defense = 100
        self.currentPos = currentPos
        self.weapon = weapon

    def move(self, currentPos):
        currentPos = WORLD[currentPos]["exits"][moveDirection]
        
    def take(self, weapon, defense):
        
        
        
    
class GameObject:
    def __init__(self, name, description):
        self.name = name
        self. description = description


class Object_Interactive(GameObject):      #work on this later to properly generalise consumables, weapons, 
    def __init__(self, )


#this class is temporary
class Weapons(Object_Interactive):
    def __init__(self, durability, damage_inflected, status, )


class Location(GameObject):
    def __init__(self, exits, items, characters, currentPos):
        self.exits = {}
        self.items = []
        self.characters = []

    def 
        

class NPCs:
    def __init__(self, name):
        self.name = name