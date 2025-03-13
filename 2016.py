import tkinter as tk
import math
import random

# Game constants
FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4
RECT_WIDTH, RECT_HEIGHT = WIDTH-200 // COLS, HEIGHT-200 // ROWS

OUTLINE_COLOR = "#BBADA0"
BACKGROUND_COLOR = "#FAF8EF"
FONT_COLOR = "#2D230E"
FONT = ("Arial", 40, "bold")

MOVE_VEL = RECT_WIDTH  

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048")
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
        self.canvas.pack()

        self.tiles = {}  
        self.draw_grid()
        self.generate_tiles()

        self.create_buttons()
        self.window.mainloop()

    def draw_grid(self):
        for row in range(1, ROWS):
            y = row * RECT_HEIGHT
            self.canvas.create_line(0, y, RECT_WIDTH, y, fill=OUTLINE_COLOR, width=5)

        for col in range(1, COLS):
            x = col * RECT_WIDTH
            self.canvas.create_line(x, 0, x, RECT_HEIGHT, fill=OUTLINE_COLOR, width=5)

    def generate_tiles(self):
        for _ in range(2):
            self.add_random_tile()

    def add_random_tile(self):
        if len(self.tiles) >= ROWS * COLS:
            return  # No space to add new tiles

        while True:
            row, col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
            if f"{row},{col}" not in self.tiles:
                self.tiles[f"{row},{col}"] = Tile(self.canvas, row, col, random.choice([2, 4]))
def up(self):
    for tile in self.tiles.values():
        tile.delete()
    self.move_tiles("up")

def down(self):
    for tile in self.tiles.values():
        tile.delete()
    self.move_tiles("down")

def left(self):
    for tile in self.tiles.values():
        tile.delete()
    self.move_tiles("left")

def right(self):    
    for tile in self.tiles.values():
        tile.delete()
    self.move_tiles("right")        

def create_buttons(self):
    up = tk.Button(self.window, text="up", command=self.up)
    down = tk.Button(self.window, text="down", command=self.down)
    left = tk.Button(self.window, text="left", command=self.left)
    right = tk.Button(self.window, text="right", command=self.right)

    up.pack()
    down.pack()
    left.pack()
    right.pack()



class Tile:
    COLORS = ["#EEE4DA", "#EDE0C8", "#F2B179", "#F59563", "#F67C5F", "#F65E3B", "#EDCF72",
              "#EDCC61", "#EDC850", "#EDC53F", "#EDC22E", "#3E3933"]

    def __init__(self, canvas, row, col, value):
        self.canvas = canvas
        self.row = row
        self.col = col
        self.value = value

    def draw(self):
        x1, y1 = self.col * RECT_WIDTH, self.row * RECT_HEIGHT
        x2, y2 = x1 + RECT_WIDTH, y1 + RECT_HEIGHT

        color = self.get_color()
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="tile")
        self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(self.value), font=FONT, tags="tile")

    def get_color(self):
        index = int(math.log2(self.value)) - 1
        return Tile.COLORS[index] if 0 <= index < len(Tile.COLORS) else "#3E3933"

    def delete(self):
        self.canvas.delete("tile")
        


if __name__ == "__main__":
    Game()
