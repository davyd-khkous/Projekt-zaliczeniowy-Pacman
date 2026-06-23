class Player:
    def __init__(self, image_path, x, y, w, h):
        self.img = loadImage(image_path)
        self.x = x
        self.y = y
        self.speed = 8
        self.w = w
        self.h = h

    def update(self, level, cell_w, cell_h):
        dx = 0
        dy = 0

        if keyPressed:
            if key == 'a' or key == 'A':
                dx = -self.speed
            elif key == 'd' or key == 'D':
                dx = self.speed
            elif key == 'w' or key == 'W':
                dy = -self.speed
            elif key == 's' or key == 'S':
                dy = self.speed

        new_x = self.x + dx
        new_y = self.y + dy

        if level.can_move_to(new_x, self.y, self.w, self.h, cell_w, cell_h):
            self.x = new_x

        if level.can_move_to(self.x, new_y, self.w, self.h, cell_w, cell_h):
            self.y = new_y

    def display(self):
        image(self.img, self.x, self.y, self.w, self.h)


class Ghost(object):
    def init(self, x, y, w, h, image_path):
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
        Ghost.init(self, x, y, w, h, "RandomGhost.png")
        self.direction = int(random(4))

    def move(self, level, cell_w, cell_h):
        dx = 0
        dy = 0

        if self.direction == 0:
            dy = -self.speed
        elif self.direction == 1:
            dy = self.speed
        elif self.direction == 2:
            dx = -self.speed
        elif self.direction == 3:
            dx = self.speed

        new_x = self.x + dx
        new_y = self.y + dy

        if level.can_move_to(new_x, new_y, self.w, self.h, cell_w, cell_h):
            self.x = new_x
            self.y = new_y
        else:
            self.direction = int(random(4))


class HunterGhost(Ghost):
    def __init__(self, x, y, w, h):
        Ghost.init(self, x, y, w, h, "HunterGhost.png")

    def move(self, pacman_x, pacman_y, level, cell_w, cell_h):
        dx = 0
        dy = 0

        if self.x < pacman_x:
            dx = self.speed
        elif self.x > pacman_x:
            dx = -self.speed

        if self.y < pacman_y:
            dy = self.speed
        elif self.y > pacman_y:
            dy = -self.speed

        if level.can_move_to(self.x + dx, self.y, self.w, self.h, cell_w, cell_h):
            self.x += dx

        if level.can_move_to(self.x, self.y + dy, self.w, self.h, cell_w, cell_h):
            self.y += dy
