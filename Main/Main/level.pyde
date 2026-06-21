class Level:
    def __init__(self):
        self.map = [
            "#############",
            "#...........#",
            "#.###.###.#.#",
            "#...........#",
            "#.#.#####.#.#",
            "#...........#",
            "#############"
        ]

        self.tile_size = 40

    def display(self):
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                tile = self.map[row][col]

                x = col * self.tile_size
                y = row * self.tile_size

                if tile == "#":
                    self.draw_wall(x, y)
                elif tile == ".":
                    self.draw_floor(x, y)

    def draw_wall(self, x, y):
        fill(50, 80, 180)
        stroke(20, 30, 90)
        rect(x, y, self.tile_size, self.tile_size)

    def draw_floor(self, x, y):
        fill(25, 25, 30)
        stroke(40, 40, 45)
        rect(x, y, self.tile_size, self.tile_size)
