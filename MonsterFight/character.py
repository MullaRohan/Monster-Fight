import random as rn


class Character:
    def __init__(this, name, health=100):
        this.name = name
        this.health = health

    def is_alive(this):
        return this.health > 0

    def give_damage(this):
        damage = rn.randint(0, this.health)
        this.health -= damage
        return damage

    def gethealth(this):
        return this.health
