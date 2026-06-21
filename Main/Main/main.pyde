from level import Level
from objects import Player, RandomGhost, HunterGhost

level = None
player = None
pinky = None
blinky = None
cell_w = 0
cell_h = 0

def setup():
    global level, player, pinky, blinky, cell_w, cell_h

    size(1920, 1080)
    imageMode(CENTER)

    level = Level()

    cell_w = width / 16.0
    cell_h = height / 9.0

    player = Player("Pacman.png", cell_w * 1.5, cell_h * 1.5, cell_w, cell_h)
    pinky = RandomGhost(cell_w * 3.5, cell_h * 3.5, cell_w, cell_h)
    blinky = HunterGhost(cell_w * 12.5, cell_h * 6.5, cell_w, cell_h)

def draw():
    background(30)

    level.display(cell_w, cell_h)

    player.update()
    pinky.move()
    blinky.move(player.x, player.y)

    player.display()
    pinky.display()
    blinky.display()
