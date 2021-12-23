import random, time
import items, world
 
class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Pillow(), items.Rock()] #Inventory on startup
        self.hp = 100 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up
        self.gold = 15
        self.currentWpn = "Nothing"

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive
 
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
         if isinstance(i, items.Weapon):
            if i.damage > max_dmg:
                max_dmg = i.damage
                best_weapon = i
 
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
     action_method = getattr(self, action.method.__name__)
     if action_method:
                action_method(**kwargs)

    def status(self):
         print("\nHP : ".self.hp)
         print("\nGold : ".self.gold)
         print("\nCurrent Weapon : ".self.currentWpn)

    def equip(self):
        print("\nThese are weapons currently possessed.\n")
        weapon_list=[]
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                weapon_list.append(item)
        i=1
        for weapon in weapon_list:
            print(i, ". ", weapon.name, sep=' ')
            i += 1

        while True:

            itemChoice = int(input("""\nSelect the weapon you want to equip: """)) - 1

            if itemChoice not in range(0, len(weapon_list)):
                print("\nInvalid weapon choice")
                # sounds.no
                continue
            break

        print('\n')
        print(weapon_list[itemChoice].name," equipped.\n")
        self.currentWpn = weapon_list[itemChoice]

    def heal(self):
        print("\nThese are the potions you currently possess.\n")
        potion_list = []

        for potion in self.inventory:
            if isinstance(potion, items.Potions):
                if potion.amt <= 0:
                    self.inventory.remove(potion)
                    continue
                else:
                    potion_list.append(potion)
            i = 1
            for potion in potion_list:
                print(i, ". ", potion.name, sep="")
                i += 1
            while True:
                if len(potion_list) == 0:
                    print("You have no potions.")
                    time.sleep(3)
                    return None

                itemChoice = int(input("""\nSelect Potion: """)) - 1

                if itemChoice not in range(0, len(potion_list)):
                    print("\nInvalid choice")
                    # sounds.no
                    continue
                break
            self.healToPlayer(itemChoice, potion_list)

    def healToPlayer(self, itemChoice, potionList):
        chosenPotion = potionList[itemChoice]