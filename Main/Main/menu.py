class Menu:
    def __init__(self):
        self.selectedMap = "Mapa"

        self.button_w = 400
        self.button_h = 90

    def display(self):
        background(10, 20, 80)

        textAlign(CENTER)

        fill(255, 255, 0)
        textSize(80)
        text("PAC-MAN", width / 2, 220)

        fill(255)
        textSize(32)
        text("Dostepna mapa: " + self.selectedMap, width / 2, 310)

        self.draw_button(width / 2 - 200, 380, "WYBIERZ MAPE", 70, 120, 255)
        self.draw_button(width / 2 - 200, 510, "GRAJ", 0, 180, 0)
        self.draw_button(width / 2 - 200, 640, "WYJDZ Z GRY", 180, 0, 0)

    def draw_button(self, x, y, label, r, g, b):
        fill(r, g, b)
        rect(x, y, self.button_w, self.button_h, 10)

        fill(255)
        textSize(32)
        text(label, x + self.button_w / 2, y + 55)

    def click(self, mx, my):
        x = width / 2 - 200

        if self.is_inside(mx, my, x, 380):
            return "map"

        if self.is_inside(mx, my, x, 510):
            return "play"

        if self.is_inside(mx, my, x, 640):
            return "exit"

        return None

    def is_inside(self, mx, my, x, y):
        return x <= mx <= x + self.button_w and y <= my <= y + self.button_h
