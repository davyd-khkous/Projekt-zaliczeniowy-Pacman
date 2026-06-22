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

                if tile == ".":
                    self.draw_coin(x, y, cell_w, cell_h)

    def draw_wall(self, x, y, w, h):
        fill(50, 80, 180)
        stroke(20, 30, 90)
        rect(x, y, w, h)

    def draw_floor(self, x, y, w, h):
        fill(25, 25, 30)
        stroke(40, 40, 45)
        rect(x, y, w, h)

    def draw_coin(self, x, y, w, h):
        fill(255, 220, 0)
        noStroke()
        ellipse(x + w / 2, y + h / 2, w * 0.15, h * 0.15)

    def collect_coins(self, player_x, player_y, player_radius, cell_w, cell_h):
        collected = 0

        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == ".":
                    coin_x = col * cell_w + cell_w / 2
                    coin_y = row * cell_h + cell_h / 2

                    if dist(player_x, player_y, coin_x, coin_y) < player_radius:
                        line = self.map[row]
                        self.map[row] = line[:col] + " " + line[col + 1:]
                        collected += 1

        return collected

    def coins_left(self):
        total = 0

        for row in self.map:
            total += row.count(".")

        return total


    def coins_left(self):
        total = 0

        for row in self.map:
            total += row.count(".")

        return total
