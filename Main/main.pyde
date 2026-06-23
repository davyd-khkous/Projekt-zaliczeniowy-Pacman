def setup():
    global player
    size(800, 600)
    imageMode(CENTER)
    player = Player("Pacman.png", 400, 300)

def draw():
    background(30)

    player.update()
    player.display()
    
class Player:
    def __init__(self, image_path, x, y):
        self.img = loadImage("Pacman.png")
        self.x = x
        self.y = y
        self.speed = 5
        self.w = 64
        self.h = 64

    def update(self):
        if keyPressed:
                if key == 'a' or key == 'A':
                    self.x -= self.speed
                elif key == 'd' or key == 'D':
                    self.x += self.speed
                elif key == 'w' or key == 'W':
                    self.y -= self.speed
                elif key == 's' or key == 'S':
                    self.y += self.speed
        
        self.x = constrain(self.x, self.w / 2, width - self.w / 2)
        self.y = constrain(self.y, self.h / 2, height - self.h / 2)

    def display(self):
        image(self.img, self.x, self.y, self.w, self.h)
        
