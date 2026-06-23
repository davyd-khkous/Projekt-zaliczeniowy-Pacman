from level import Level
from objects import Player, RandomGhost, HunterGhost
from menu import Menu

MENU = 0
GAME = 1
GAME_OVER = 2

gameState = MENU

level = None
player = None
pinky = None
blinky = None
menu = None

cell_w = 0
cell_h = 0
score = 0


def setup():
    global menu

    size(1920, 1080)
    imageMode(CENTER)

    menu = Menu()


def startGame():
    global level, player, pinky, blinky, cell_w, cell_h, score

    level = Level()

    cell_w = width / 16.0
    cell_h = height / 9.0

    player = Player("Pacman.png", cell_w * 1.5, cell_h * 1.5, cell_w, cell_h)
    pinky = RandomGhost(cell_w * 3.5, cell_h * 3.5, cell_w, cell_h)
    blinky = HunterGhost(cell_w * 13.5, cell_h * 6.5, cell_w, cell_h)

    score = 0


def draw():
    if gameState == MENU:
        menu.display()

    elif gameState == GAME:
        drawGame()
        
    elif gameState == GAME_OVER:
        drawGameOver()


def drawGame():
    global score, gameState

    background(30)

    player.update(level, cell_w, cell_h)
    pinky.move(level, cell_w, cell_h)
    blinky.move(player.x, player.y, level, cell_w, cell_h)

    score += level.collect_coins(player.x, player.y, player.w / 2, cell_w, cell_h)
    
    check_collision(pinky)
    check_collision(blinky)
    
    if player.hp <= 0:
        gameState = GAME_OVER

    level.display(cell_w, cell_h)

    player.display()
    pinky.display()
    blinky.display()

    fill(255)
    textAlign(LEFT)
    textSize(32)
    text("Wynik: " + str(score), 20, 40)
    text("Zycia: " + str(player.hp), width - 150, 40)

    if level.coins_left() == 0:
        textAlign(CENTER)
        textSize(60)
        text("Poziom ukonczony!", width / 2, height / 2)
        textSize(30)
        text("Nacisnij M, aby przejsc do menu", width / 2, height / 2 + 60)

def resetGame():
    global level, player, pinky, blinky
    global score

    level = Level()

    player = Player(
        "Pacman.png",
        cell_w * 1.5,
        cell_h * 1.5,
        cell_w,
        cell_h
    )

    pinky = RandomGhost(
        cell_w * 3.5,
        cell_h * 3.5,
        cell_w,
        cell_h
    )

    blinky = HunterGhost(
        cell_w * 13.5,
        cell_h * 6.5,
        cell_w,
        cell_h
    )

    score = 0

def keyPressed():
    global game_state

    if game_state == GAME and level.coins_left() == 0:

        if key == 'm' or key == 'M':

            resetGame()

            menu.start_game = False

            game_state = MENU

def check_collision(ghost):
    distance = dist(player.x, player.y, ghost.x, ghost.y)
    if distance < (player.w * 0.4 + ghost.w * 0.4) and player.invulnerable_timer <= 0:
        player.hp -= 1
        player.invulnerable_timer = 90
        
def drawGameOver():
    background(20, 0, 0)
    fill(255, 0, 0)
    textAlign(CENTER)
    textSize(100)
    text("PRZEGRANA", width / 2, height / 2 - 50)

def mousePressed():
    global gameState

    if gameState == MENU:
        action = menu.click(mouseX, mouseY)

        if action == "map":
            print("Wybrana mapa:", menu.selectedMap)

        elif action == "play":
            startGame()
            gameState = GAME

        elif action == "exit":
            exit()
