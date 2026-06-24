class Menu:
    # Stan początkowy menu
    def __init__(self):
        self.selectedMap = "Poziom 1"
        # Globalne wymiary przycisków
        self.button_w = 400
        self.button_h = 90
        
        
    # Renderowanie UI - Rysowanie tła, tytułu i przycisków
    def display(self):
        background(0)
        
        textAlign(CENTER)
        
        # Tytuł główny gry
        fill(255, 255, 0)
        textSize(80)
        text("PAC-MAN", width / 2, 220)
        
        # Wyświetlanie aktualnie wybranego poziomu
        fill(255)
        textSize(32)
        text("Dostepna mapa: " + self.selectedMap, width / 2, 310)
        
        # Generowanie przycisków z podanymi kolorami
        self.draw_button(width / 2 - 200, 380, self.selectedMap, 50, 80, 180)
        self.draw_button(width / 2 - 200, 510, "GRAJ", 0, 120, 0)
        self.draw_button(width / 2 - 200, 640, "WYJDZ Z GRY", 150, 0, 0)
        
        
    # Rysuje prostokąt z obramowaniem i wyśrodkowanym tekstem
    def draw_button(self, x, y, label, r, g, b):
        fill(r, g, b)
        stroke(255)
        strokeWeight(5)
        
        rect(x, y, self.button_w, self.button_h)
        
        fill(255)
        textSize(24)
        # Matematyczne wyśrodkowanie tekstu względem rozmiaru przycisku
        text(label, x + self.button_w / 2, y + self.button_h / 2 + 10)

    # Przełącznik (toggle) do zmiany poziomu i stopnia trudności
    def toggle_map(self):
        if self.selectedMap == "Poziom 1":
            self.selectedMap = "Poziom 2"
        else:
            self.selectedMap = "Poziom 1"


    # Sprawdza, czy współrzędne myszy (mx, my) znajdują się wewnątrz prostokątów przycisków
    def click(self, mx, my):
        # Detekcja dla przycisku zmiany mapy
        if mx > width / 2 - 200 and mx < width / 2 + 200 and my > 380 and my < 380 + 90:
            return "map"
        # Detekcja dla przycisku startu gry   
        elif mx > width / 2 - 200 and mx < width / 2 + 200 and my > 510 and my < 510 + 90:
            return "play"
        # Detekcja dla przycisku wyjści    
        elif mx > width / 2 - 200 and mx < width / 2 + 200 and my > 640 and my < 640 + 90:
            return "exit"
        # Zwraca None, jeśli kliknięto w puste tło    
        return None
