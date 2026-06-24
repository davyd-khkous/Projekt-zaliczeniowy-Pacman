class Menu:
    def __init__(self):
        self.selectedMap = "Poziom 1"
        
        self.button_w = 400
        self.button_h = 90
        
    def display(self):
        background(0)
        
        textAlign(CENTER)
        
        fill(255, 255, 0)
        textSize(80)
        text("PAC-MAN", width / 2, 220)
        
        fill(255)
        textSize(32)
        text("Dostepna mapa: " + self.selectedMap, width / 2, 310)
        
        self.draw_button(width / 2 - 200, 380, self.selectedMap, 50, 80, 180)
        self.draw_button(width / 2 - 200, 510, "GRAJ", 0, 120, 0)
        self.draw_button(width / 2 - 200, 640, "WYJDZ Z GRY", 150, 0, 0)
        
    def draw_button(self, x, y, label, r, g, b):
        fill(r, g, b)
        stroke(255)
        strokeWeight(5)
        
        rect(x, y, self.button_w, self.button_h)
        
        fill(255)
        textSize(24)
        text(label, x + self.button_w / 2, y + self.button_h / 2 + 10)

    def toggle_map(self):
        if self.selectedMap == "Poziom 1":
            self.selectedMap = "Poziom 2"
        else:
            self.selectedMap = "Poziom 1"

    def click(self, mx, my):
        if mx > width / 2 - 200 and mx < width / 2 + 200 and my > 380 and my < 380 + 90:
            return "map"
            
        elif mx > width / 2 - 200 and mx < width / 2 + 200 and my > 510 and my < 510 + 90:
            return "play"
            
        elif mx > width / 2 - 200 and mx < width / 2 + 200 and my > 640 and my < 640 + 90:
            return "exit"
            
        return None
