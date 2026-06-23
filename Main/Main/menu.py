
MENU = 0
GAME = 1

gameState = MENU

selectedMap = "Mapa"


def setup():
    size(800, 600)


def draw():

    if gameState == MENU:
        drawMenu()

    elif gameState == GAME:
        drawGame()


def drawMenu():

    background(10, 20, 80)

    textAlign(CENTER)


    fill(255, 255, 0)
    textSize(40)
    text("PAC-MAN", width/2, 120)


    fill(255)
    textSize(20)
    text("Dostępna mapa: " + selectedMap, width/2, 180)


    fill(70, 120, 255)
    rect(250, 230, 300, 70, 10)

    fill(255)
    textSize(24)
    text("WYBIERZ MAPĘ", width/2, 275)


    fill(0, 180, 0)
    rect(250, 330, 300, 70, 10)

    fill(255)
    text("GRAJ", width/2, 375)


    fill(180, 0, 0)
    rect(250, 430, 300, 70, 10)

    fill(255)
    text("WYJDŹ Z GRY", width/2, 475)


def drawGame():

    background(0)

    fill(255)
    textSize(24)
    textAlign(LEFT)

    text("Mapa: " + selectedMap, 20, 40)




def mousePressed():

    global gameState

    if gameState == MENU:

    
        if (250 <= mouseX <= 550 and
            230 <= mouseY <= 300):
            print("Wybrana mapa:", selectedMap)

    
        elif (250 <= mouseX <= 550 and
              330 <= mouseY <= 400):
            gameState = GAME

    
        elif (250 <= mouseX <= 550 and
              430 <= mouseY <= 500):
            exit()
