from level import Level
from objects import Player

level = None
player = None

def setup():
    global level, player, pinky, blinky

    size(800, 600)
    imageMode(CENTER)

    level = Level()
    player = Player("Pacman.png", 400, 300)
    pinky = RandomGhost(100, 100)
    blinky = HunterGhost(700, 500)

def draw():
    background(30)

    level.display()
    player.update()
    player.display()
    pinky.move()
    pinky.displaj()
    blinky.move(player.x, player.y)
    blinky.display()
