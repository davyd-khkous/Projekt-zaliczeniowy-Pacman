class Player:
    def __init__(self, image_path, x, y, w, h):
        self.img = loadImage(image_path)
        self.x = x
        self.y = y
        self.speed = 8
        self.w = w
        self.h = h
        self.flip_x = False

    def update(self, level, cell_w, cell_h):
        dx = 0
        dy = 0

        if keyPressed:
            if key == 'a' or key == 'A':
                dx = -self.speed
                self.flip_x = True
            elif key == 'd' or key == 'D':
                dx = self.speed
                self.flip_x = False
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
        pushMatrix()
        translate(self.x, self.y)

        if self.flip_x:
            scale(-1, 1)

        image(self.img, 0, 0, self.w, self.h)

        popMatrix()


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
        Ghost.__init__(self, x, y, w, h, "HunterGhost.png")

    def move(self, pacman_x, pacman_y, level, cell_w, cell_h):
        diff_x = pacman_x - self.x
        diff_y = pacman_y - self.y

        move_x = self.speed if diff_x > 0 else -self.speed if diff_x < 0 else 0
        move_y = self.speed if diff_y > 0 else -self.speed if diff_y < 0 else 0

        if abs(diff_x) > abs(diff_y):
            primary_axis = 'x'; primary_move = move_x
            secondary_axis = 'y'; secondary_move = move_y
        else:
            primary_axis = 'y'; primary_move = move_y
            secondary_axis = 'x'; secondary_move = move_x

        moved = False

        if primary_axis == 'x' and primary_move != 0:
            if level.can_move_to(self.x + primary_move, self.y, self.w, self.h, cell_w, cell_h):
                self.x += primary_move
                moved = True
        elif primary_axis == 'y' and primary_move != 0:
            if level.can_move_to(self.x, self.y + primary_move, self.w, self.h, cell_w, cell_h):
                self.y += primary_move
                moved = True

        if not moved:
            if primary_axis == 'x':
                if secondary_move == 0:
                    if level.can_move_to(self.x, self.y + self.speed, self.w, self.h, cell_w, cell_h):
                        self.y += self.speed
                    elif level.can_move_to(self.x, self.y - self.speed, self.w, self.h, cell_w, cell_h):
                        self.y -= self.speed
                elif level.can_move_to(self.x, self.y + secondary_move, self.w, self.h, cell_w, cell_h):
                    self.y += secondary_move
                    
            elif primary_axis == 'y':
                if secondary_move == 0:
                    if level.can_move_to(self.x + self.speed, self.y, self.w, self.h, cell_w, cell_h):
                        self.x += self.speed
                    elif level.can_move_to(self.x - self.speed, self.y, self.w, self.h, cell_w, cell_h):
                        self.x -= self.speed
                elif level.can_move_to(self.x + secondary_move, self.y, self.w, self.h, cell_w, cell_h):
                    self.x += secondary_move
