from level import Level
from objects import Player, RandomGhost, HunterGhost
from menu import Menu

MENU = 0
GAME = 1
GAME_OVER = 2
LEVEL_COMPLETE = 3

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

    level = Level(menu.selectedMap)

    cols = len(level.map[0])
    rows = len(level.map)
    
    cell_w = width / float(cols)
    cell_h = height / float(rows)

    player = Player("Pacman.png", "Pacman2.png", cell_w * 1.5, cell_h * 1.5, cell_w, cell_h)
    pinky = RandomGhost(cell_w * 3.5, cell_h * 3.5, cell_w, cell_h)
    
    if menu.selectedMap == "Poziom 2":
        blinky = HunterGhost(cell_w * 17.5, cell_h * 10.5, cell_w, cell_h)
        pinky.speed = 4
        blinky.speed = 4
    else:
        blinky = HunterGhost(cell_w * 13.5, cell_h * 6.5, cell_w, cell_h)
        pinky.speed = 2
        blinky.speed = 2

    score = 0


def draw():
    if gameState == MENU:
        menu.display()

    elif gameState == GAME:
        drawGame()

    elif gameState == GAME_OVER:
        drawGameOver()

    elif gameState == LEVEL_COMPLETE:
        drawLevelComplete()


def drawGame():
    global score, gameState

    background(30)

    player.update(level, cell_w, cell_h)
    pinky.move(level, cell_w, cell_h)
    blinky.move(player.x, player.y, level, cell_w, cell_h)

    collected = level.collect_coins(player.x, player.y, player.w / 2, cell_w, cell_h)

    if collected > 0:
        player.eat()

    score += collected

    check_collision(pinky)
    check_collision(blinky)

    if player.hp <= 0:
        gameState = GAME_OVER

    elif level.coins_left() == 0:
        gameState = LEVEL_COMPLETE

    level.display(cell_w, cell_h)

    player.display()
    pinky.display()
    blinky.display()

    drawInterface()


def drawInterface():
    fill(80)
    stroke(255)
    strokeWeight(3)
    rect(15, 15, 180, 45)
    rect(width - 195, 15, 180, 45)
 
    fill(255)
    textSize(24)
    textAlign(LEFT)
    text("Wynik: " + str(score), 30, 45)

    textAlign(LEFT)
    text("Zycia: " + str(player.hp), width - 175, 45)


def check_collision(ghost):
    distance_to_ghost = dist(player.x, player.y, ghost.x, ghost.y)
    collision_distance = player.w * 0.4 + ghost.w * 0.4

    if distance_to_ghost < collision_distance and player.invulnerable_timer <= 0:
        player.hp -= 1
        player.invulnerable_timer = 120
        player.reset_position()


def drawGameOver():
    background(0)

    fill(150, 0, 0)
    stroke(255, 0, 0)
    strokeWeight(5)
    rect(width / 2 - 250, height / 2 - 150, 500, 300)

    fill(255)
    textAlign(CENTER)
    textSize(60)
    text("PRZEGRANA :(", width / 2, height / 2 - 20)

    textSize(24)
    text("Kliknij zeby wrocic", width / 2, height / 2 + 60)


def drawLevelComplete():
    background(0)

    fill(0, 120, 0)
    stroke(0, 255, 0)
    strokeWeight(5)
    rect(width / 2 - 250, height / 2 - 150, 500, 300)

    fill(255)
    textAlign(CENTER)
    textSize(60)
    text("WYGRANA!!!", width / 2, height / 2 - 20)

    textSize(24)
    text("Kliknij zeby wrocic", width / 2, height / 2 + 60)


def mousePressed():
    global gameState

    if gameState == MENU:
        action = menu.click(mouseX, mouseY)

        if action == "map":
            menu.toggle_map() # Тепер кнопка викликає перемикання карти!
            print("Wybrana mapa:", menu.selectedMap)

        elif action == "play":
            startGame()
            gameState = GAME

        elif action == "exit":
            exit()

    elif gameState == GAME_OVER or gameState == LEVEL_COMPLETE:
        gameState = MENU


def keyPressed():
    if gameState == GAME:
        player.press_key(key)


def keyReleased():
    if gameState == GAME:
        player.release_key(key)

