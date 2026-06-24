from level import Level
from objects import Player, RandomGhost, HunterGhost
from menu import Menu

# Zmienne definiujące aktualny etap gry tzw Maszyna stanów

MENU = 0
GAME = 1
GAME_OVER = 2
LEVEL_COMPLETE = 3
gameState = MENU

# Globalne obiekty gry

level = None
player = None
pinky = None
blinky = None
menu = None

cell_w = 0
cell_h = 0
score = 0

# Inicjalizacja okna gry i głównego menu

def setup():
    global menu
    size(1920, 1080)
    imageMode(CENTER)
    menu = Menu()

# Start gry - generowanie poziomu i postaci

def startGame():
    global level, player, pinky, blinky, cell_w, cell_h, score
    level = Level(menu.selectedMap)

    # Obliczamy rozmiar komórki, aby dowolna mapa idealnie wpasowała się w ekran
    cols = len(level.map[0])
    rows = len(level.map)
        
    cell_w = width / float(cols)
    cell_h = height / float(rows)
    
    # Bezpieczny spawn gracza i losowego ducha
    player = Player("Pacman.png", "Pacman2.png", cell_w * 1.5, cell_h * 1.5, cell_w, cell_h)
    pinky = RandomGhost(cell_w * 3.5, cell_h * 3.5, cell_w, cell_h)
    
    # Poziomem trudności (prędkość i bezpieczny spawn dla ducha "Hunter")
    if menu.selectedMap == "Poziom 2":
        blinky = HunterGhost(cell_w * 17.5, cell_h * 10.5, cell_w, cell_h)
        pinky.speed = 4
        blinky.speed = 4
    else:
        blinky = HunterGhost(cell_w * 13.5, cell_h * 6.5, cell_w, cell_h)
        pinky.speed = 2
        blinky.speed = 2
    score = 0

#Główna pętla gry 
#Przełącza ekrany w zależności od aktualnego stanu maszyny stanów
    
def draw():
    if gameState == MENU:
        menu.display()

    elif gameState == GAME:
        drawGame()

    elif gameState == GAME_OVER:
        drawGameOver()

    elif gameState == LEVEL_COMPLETE:
        drawLevelComplete()

# Aktualizacja logiki i renderowanie klatek

def drawGame():
    global score, gameState

    background(30)
    
    # Ruch postaci
    player.update(level, cell_w, cell_h)
    pinky.move(level, cell_w, cell_h)
    blinky.move(player.x, player.y, level, cell_w, cell_h) # HunterGhost śledzi gracza

    # Zbieranie punktów
    collected = level.collect_coins(player.x, player.y, player.w / 2, cell_w, cell_h)

    if collected > 0:
        player.eat()

    score += collected

    # Sprawdzanie interakcji gracz-przeciwnik
    check_collision(pinky)
    check_collision(blinky)

    # Warunki zakończenia gry
    if player.hp <= 0:
        gameState = GAME_OVER

    elif level.coins_left() == 0:
        gameState = LEVEL_COMPLETE

    # Renderowanie grafiki
    level.display(cell_w, cell_h)
    player.display()
    pinky.display()
    blinky.display()
    drawInterface()

# Rysowanie minimalistycznego interfejsu
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

#System kolizji
def check_collision(ghost):
    distance_to_ghost = dist(player.x, player.y, ghost.x, ghost.y)
    collision_distance = player.w * 0.4 + ghost.w * 0.4

    #System szkody i niezniszczalności 2 sekundy po 
    if distance_to_ghost < collision_distance and player.invulnerable_timer <= 0:
        player.hp -= 1
        player.invulnerable_timer = 120
        player.reset_position()

# Widok przegranej
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

# Widok wygranej
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

# Obsługa zdarzeń myszki dla menu i ekranów końcowych
def mousePressed():
    global gameState

    if gameState == MENU:
        action = menu.click(mouseX, mouseY)

        if action == "map":
            menu.toggle_map() 
            print("Wybrana mapa:", menu.selectedMap)

        elif action == "play":
            startGame()
            gameState = GAME

        elif action == "exit":
            exit()

    elif gameState == GAME_OVER or gameState == LEVEL_COMPLETE:
        gameState = MENU

# Wciśnięcie klawisza ruchu
def keyPressed():
    if gameState == GAME:
        player.press_key(key)

# Puszczenie klawisza ruchu
def keyReleased():
    if gameState == GAME:
        player.release_key(key)

