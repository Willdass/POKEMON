


class Pokemon:
    def __init__(self, name, level, race, max_health, current_health, is_knocked_out):
        self.name = name
        self.level = level
        self.race = race
        self.max_health = level
        self.current_health = current_health
        self.is_knocked_out = is_knocked_out

    def knocked_out(self):
        if self.current_health <= self.is_knocked_out:
            return "{} now is OUT !".format(self.name)

    def lose_health(self, perte):
        self.current_health -= perte
        if self.current_health <= self.is_knocked_out:
            return self.knocked_out()
        else:
            return "{} now has {} health".format(self.name, self.current_health)

    def gain_health(self, gain):
        self.current_health = self.current_health + gain
        return "{} now has {} health".format(self.name, self.current_health)

    def attack(self):
        pokemon_2 = input("De quel race est ton pokemon adverse ? FIRE, WATER, WIND, ROCK")
        if self.race.upper() == "FIRE" or self.race.upper() == "ROCK" and pokemon_2 == "FIRE":
            perte = self.current_health - 10
            if perte < 10:
                perte = 15
            return self.lose_health(perte)
        elif self.race.upper() == "WATER" or self.race.upper() == "WIND" and pokemon_2 == "FIRE":
            perte = self.current_health - 15
            if perte < 10:
                perte = 15
            return self.lose_health(perte)
        elif self.race.upper() == "FIRE" or self.race.upper() == "ROCK" and pokemon_2 == "WATER":
            perte = self.current_health - 10
            if perte < 10:
                perte = 15
            return self.lose_health(perte)
        elif self.race.upper() == "WATER" or self.race.upper() == "WIND" and pokemon_2 == "WATER":
            perte = self.current_health - 15
            if perte < 10:
                perte = 15
            return self.lose_health(perte)
        elif self.race.upper() == "FIRE" or self.race.upper() == "ROCK" and pokemon_2 == "WIND":
            perte = self.current_health - 15
            if perte < 10:
                perte = 15
            return self.lose_health(perte)
        elif self.race.upper() == "WATER" or self.race.upper() == "WIND" and pokemon_2 == "WIND":
            perte = self.current_health - 10
            if perte < 10:
                perte = 15
            return self.lose_health(perte)
        elif self.race.upper() == "FIRE" or self.race.upper() == "ROCK" and pokemon_2 == "ROCK":
            perte = self.current_health - 10
            if perte < 10:
                perte = 15
            return self.lose_health(perte)
        elif self.race.upper() == "WATER" or self.race.upper() == "WIND" and pokemon_2 == "ROCK":
            perte = self.current_health - 15
            if perte < 10:
                perte = 15
            return self.lose_health(perte)


n = Pokemon("Salameche", 30, "fire", 30, 30, 0)
print(n.attack())
print(n.attack())
