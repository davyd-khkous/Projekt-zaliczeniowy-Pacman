from level import Level
from objects import Player

level = None
player = None

def setup():
    global level, player

    size(800, 600)
    imageMode(CENTER)

    level = Level()
    player = Player("Pacman.png", 400, 300)

def draw():
    background(30)

    level.display()
    player.update()
    player.display()
