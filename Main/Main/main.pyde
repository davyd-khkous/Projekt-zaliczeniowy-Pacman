from level import Level
from objects import Player, RandomGhost, HunterGhost
from menu import Menu
MENU = 0
GAME = 1

game_state = MENU
menu = None
level = None
player = None
pinky = None
blinky = None
cell_w = 0
cell_h = 0
score = 0

def setup():
    global level, player, pinky, blinky, cell_w, cell_h, menu

    size(1920, 1080)
    imageMode(CENTER)
    menu = Menu()

    level = Level()

    cell_w = width / 16.0
    cell_h = height / 9.0

    player = Player("Pacman.png", cell_w * 1.5, cell_h * 1.5, cell_w, cell_h)
    pinky = RandomGhost(cell_w * 3.5, cell_h * 3.5, cell_w, cell_h)
    blinky = HunterGhost(cell_w * 13.5, cell_h * 6.5, cell_w, cell_h)

def draw():
    global score, game_state
    if game_state == MENU:

        menu.display()

        if menu.start_game:
            game_state = GAME

    elif game_state == GAME:
    background(30)

    player.update(level, cell_w, cell_h)
    pinky.move(level, cell_w, cell_h)
    blinky.move(player.x, player.y, level, cell_w, cell_h)

    score += level.collect_coins(player.x, player.y, player.w / 2, cell_w, cell_h)

    level.display(cell_w, cell_h)

    player.display()
    pinky.display()
    blinky.display()

    fill(255)
    textSize(32)
    text("Wynik: " + str(score), 20, 40)

    if level.coins_left() == 0:
        textSize(60)
        text("Poziom ukonczony!", width / 2 - 250, height / 2)

def mousePressed():

    if game_state == MENU:
        menu.mousePressed()
