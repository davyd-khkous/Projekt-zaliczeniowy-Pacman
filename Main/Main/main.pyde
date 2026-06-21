from level import Level
from objects import Player

level = None
player = None
cell_w = 0
cell_h = 0

def setup():
    global level, player, cell_w, cell_h

    size(1920, 1080)
    imageMode(CENTER)

    level = Level()

    cell_w = width / 16.0
    cell_h = height / 9.0

    player = Player("Pacman.png", cell_w * 1.5, cell_h * 1.5, cell_w, cell_h)

def draw():
    background(30)

    level.display(cell_w, cell_h)
    player.update()
    player.display()
