class Player:
    def __init__(self, image_path, x, y, w, h):
        self.img = loadImage(image_path)
        self.x = x
        self.y = y
        self.speed = 8
        self.w = w
        self.h = h

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


class Ghost(object):
    def __init__(self, x, y, w, h, image_path):
        self.x = x
        self.y = y
        self.speed = 2
        self.img = loadImage(image_path)
        self.w = w
        self.h = h

    def display(self):
        image(self.img, self.x, self.y, self.w, self.h)


class RandomGhost(Ghost):
    def __init__(self, x, y, w, h):
        Ghost.__init__(self, x, y, w, h, "RandomGhost.png")
        self.direction = int(random(4))

    def move(self):
        if self.direction == 0:
            self.y -= self.speed
        elif self.direction == 1:
            self.y += self.speed
        elif self.direction == 2:
            self.x -= self.speed
        elif self.direction == 3:
            self.x += self.speed

        if self.x < self.w / 2 or self.x > width - self.w / 2 or self.y < self.h / 2 or self.y > height - self.h / 2:
            self.direction = int(random(4))

        self.x = constrain(self.x, self.w / 2, width - self.w / 2)
        self.y = constrain(self.y, self.h / 2, height - self.h / 2)


class HunterGhost(Ghost):
    def __init__(self, x, y, w, h):
        Ghost.__init__(self, x, y, w, h, "HunterGhost.png")

    def move(self, pacman_x, pacman_y):
        if self.x < pacman_x:
            self.x += self.speed
        elif self.x > pacman_x:
            self.x -= self.speed

        if self.y < pacman_y:
            self.y += self.speed
        elif self.y > pacman_y:
            self.y -= self.speed

        self.x = constrain(self.x, self.w / 2, width - self.w / 2)
        self.y = constrain(self.y, self.h / 2, height - self.h / 2)
