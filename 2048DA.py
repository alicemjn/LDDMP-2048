import tkinter as tk
import math
import random  

FPS = 60
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4

RECT_WIDTH, RECT_HEIGHT = WIDTH // COLS, HEIGHT // ROWS

OUTLINE_COLOR = "#BBADA0"
BACKGROUND_COLOR = "#FAF8EF"
FONT_SIZE = 40
OUTLINE_THICKNESS = 8
FONT_COLOR = "#2D230E"
FONT = ("Arial", 40, "bold")

MOVE_VEL = 20

def get_random_pos(tiles):
    while True:
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLS - 1)
        if f"{row},{col}" not in tiles:
            return row, col  

def generate_tiles(canvas):
    tiles = {}
    for _ in range(2) :
        row, col = get_random_pos(tiles)
        tiles[f"{row},{col}"] = Tile(canvas, row, col, 2) 
    return tiles  

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048")
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
        self.canvas.pack()
        self.draw_grid()
        
        # Generate initial tiles
        self.tiles = generate_tiles(self.canvas)

        self.window.mainloop()

    def draw_grid(self):
        for row in range(1, ROWS):
            y = row * RECT_HEIGHT
            self.canvas.create_line(0, y, WIDTH, y, fill=OUTLINE_COLOR, width=OUTLINE_THICKNESS)

        for col in range(1, COLS):
            x = col * RECT_WIDTH
            self.canvas.create_line(x, 0, x, HEIGHT, fill=OUTLINE_COLOR, width=OUTLINE_THICKNESS)

        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, outline=OUTLINE_COLOR, width=OUTLINE_THICKNESS)

class Tile:
    COLORS = ["#EEE4DA", "#EDE0C8", "#F2B179", "#F59563", "#F67C5F", "#F65E3B", "#EDCF72",
              "#EDCC61", "#EDC850", "#EDC53F", "#EDC22E", "#3E3933"]

    def __init__(self, canvas, row, col, value):
        self.canvas = canvas
        self.row = row
        self.col = col
        self.value = value
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT
        self.color = self.get_color()
        self.draw()

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        return Tile.COLORS[color_index] if 0 <= color_index < len(Tile.COLORS) else "#3E3933"

    def draw(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + RECT_WIDTH, self.y + RECT_HEIGHT, fill=self.color)
        self.canvas.create_text(self.x + RECT_WIDTH // 2, self.y + RECT_HEIGHT // 2, text=str(self.value),
                                fill=FONT_COLOR, font=FONT)

if __name__ == "__main__":
    Game()