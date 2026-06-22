from level import Level
from objects import Player, RandomGhost, HunterGhost

level = None
player = None
pinky = None
blinky = None
cell_w = 0
cell_h = 0
score = 0

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
    global score

    background(30)

    level.display(cell_w, cell_h)

    player.update()
    pinky.move()
    blinky.move(player.x, player.y)

    score += level.collect_coins(player.x, player.y, player.w / 2, cell_w, cell_h)

    player.display()
    pinky.display()
    blinky.display()

    fill(255)
    textSize(32)
    text("Wynik: " + str(score), 20, 40)

    if level.coins_left() == 0:
        textSize(60)
        text("Poziom ukonczony!", width / 2 - 250, height / 2)
