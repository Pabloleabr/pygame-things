
_moves = {"scrash" : [20, "atk", None], "tail atack" : [30, "atk", None], "super omega op move": [999, "atk", None],
                 "rage": [0.5,"buff", "atk"], "ironskin":[0.5, "buff", "deff"], "epic punch": [40, "atk", None], "fire ball" : [50, "atk", None]}

Pokemons = {"charmander": [80, 15, 9, 11, ["scratch", "tail atack", "fire ball", "rage"]], "squiertail":[86, 13, 13, 8, ["scratch", "tail atack", "epic punch", "ironskin"]],
            "Godtest":[666, 666, 666, 1, ["super omega op move", "", "", ""]]}

class pokemon():
    def __init__(self, name, health, atk, deff, speed, move_set):
        """debe introducirse el nombre, vida, ataque, defence, velociadad, una lista con sus movimientos """
        self.name = name
        self.maxhealth = health
        self.atk = atk
        self.atktemp = atk
        self.deff = deff
        self.defftemp = deff
        self.speed = speed
        self.move_set = move_set
        self.current_health = health
        self.img = name + ".png"

    def poke_img(self):
        return self.img

    def select_move(self,move_pos):
        """toma la posicion posicion en la que esta el movimiento yte devuelve su nombre, valor, tipo the buff si es un buff"""
        move = self.move_set[move_pos]
        buff = None
        if _moves[move][1] == "buff":
            buff = _moves[move][2]
        return (move, _moves[move][0], buff)


    def take_damage(self, damageOriginal):
        damage = damageOriginal - self.deff
        if damage < 1:
            damage = 1
        if damage > self.current_health:
             self.current_health = 0
        else:
            self.current_health -= damage

    def buff(self, buff, stat):
        if stat == "atk":
            self.atktemp += (self.atk * buff)
        elif stat == "def":
            self.defftemp += (self.deff * buff)
    
    def use_move(self, move_pos, pokemon2):
        """Toma la posicion del movimiento del pokemon y el pokemon al quien lo va a utilizar """
        move = pokemon.select_move(move_pos)
        if move[2] == None:
            pokemon2.take_damage(move[1] + self.atktemp)
        else:
            pokemon.buff(move[1], move[2])

    def pokemon_Cstats(self):
        return {"HP":self.current_health, "atk":self.atktemp, "def": self.defftemp, "speed":self.speed }


    def speed_check(self, pokemon2):
        """ takes the other pokemon and returns False if the pokemon past has an argument is faster"""
        return pokemon.pokemon_Cstats()["speed"] > pokemon2.pokemon_Cstats()["speed"]







