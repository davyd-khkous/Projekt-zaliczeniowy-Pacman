class Level:
    def __init__(self):
        self.map = [
            "################",
            "#..............#",
            "#.####..####...#",
            "#..............#",
            "#...##....##...#",
            "#..............#",
            "#..####..####..#",
            "#..............#",
            "################"
        ]

    def display(self, cell_w, cell_h):
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                tile = self.map[row][col]

                x = col * cell_w
                y = row * cell_h

                if tile == "#":
                    self.draw_wall(x, y, cell_w, cell_h)
                else:
                    self.draw_floor(x, y, cell_w, cell_h)

    def draw_wall(self, x, y, w, h):
        fill(50, 80, 180)
        stroke(20, 30, 90)
        rect(x, y, w, h)

    def draw_floor(self, x, y, w, h):
        fill(25, 25, 30)
        stroke(40, 40, 45)
        rect(x, y, w, h)
