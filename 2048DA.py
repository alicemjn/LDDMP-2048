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
def func(x):
    return x.col
def move_tiles(tiles, direction):
    updated=True
    Blocks=set()
    
    if direction == "left":
        sort_func = lambda x: x.col
        reverse=False
        delta=(-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tile.get(f"{tile.row},{tile.col-1}")
        merge_check=lambda tile, next_tile: tile.x>next_tile.x+MOVE_VEL
        move_check=lambda tile,next tile: tile.x>next_tile.x+RECT_WIDTH+MOVE_VEL
        ceil=True

    elif direction == "right":

        sort_func = lambda x: x.col
        reverse=True
        delta=(MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == COLS - 1
        get_next_tile = lambda tile: tile.get(f"{tile.row},{tile.col+1}")
        merge_check=lambda tile, next_tile: tile.x<next_tile.x-MOVE_VEL
        move_check=lambda tile,next tile: tile.x+RECT_WIDTH+MOVE_VEL)
    
        ceil=False

    elif direction == "up":
        sort_func = lambda x: x.row
        reverse=False
        delta=(0,-MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tile.get(f"{tile.row-1},{tile.col}")
        merge_check=lambda tile, next_tile: tile.y>next_tile.y+MOVE_VEL
        move_check=lambda tile,next tile: tile.y>next_tile.y+RECT_HEIGHT+MOVE_VEL
        ceil=True

    elif direction == "down":
        sort_func = lambda x: x.row
        reverse=True
        delta=(0,MOVE_VEL)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tile.get(f"{tile.row+1},{tile.col}")
        merge_check=lambda tile, next_tile: tile.y<next_tile.y-MOVE_VEL
        move_check=lambda tile,next tile: tile.y+RECT_HEIGHT+MOVE_VEL<next_tile.y
        ceil=False
    
    while updated:
        updated=False
        sorted_tiles=sorted(tiles.values(), key=sort_func, reverse=reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue

            next_tile=get_next_tile(tile)
            if not next_tile:
                tile.move(delta)

            elif tile.value==next_tile.value and tile not in Blocks next_tile not in Blocks:
                if merge_check(tile, next_tile):
                    tile.move(delta)
                else:
                    next_tile.value*=2
                    sorted_tiles.pop(i)
                    Blocks.add(next_tile) 

            elif move_check(tile, next_tile):
                tile.move(delta)
            else:
                continue       
            tile.set_pos(ceil)
            updated=True    

    def update_tiles(tiles, sorted_tiles):
        tiles.clear()
        for tile in sorted_tiles:
            tiles[f"{tile.row},{tile.col}"] = tile

    update_tiles(tiles, sorted_tiles)

    return end_move=set(tiles) 

    def end_move(tiles):
        if len(tiles)==16:
            return "lost"
        
        row,col=get_random_pos(tiles)
        tiles[f"{row},{col}"]=Tile(random.choice([2,4]), row, col)
        return "continue"


        
    def update_tiles(tiles, sorted_tiles):
            tiles.clear()
            for tile in sorted_tiles:
                tiles[f"{tile.row},{tile.col}"] = tile

    tile.draw()  


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                end_move = move_tiles(tiles, "left")
            elif event.key == pygame.K_RIGHT:
                end_move = move_tiles(tiles, "right")
            elif event.key == pygame.K_UP:
                end_move = move_tiles(tiles, "up")
            elif event.key == pygame.K_DOWN:
                end_move = move_tiles(tiles, "down")

            if end_move == "lost":
                print("You lost!")
                run = False
            elif end_move == "continue":
                pass

    pygame.display.update()
    clock.tick(FPS)          
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
     def set_pos(self,ceil=False):
         if ceil:
             self.row=math.ceil(self.y/RECT_HEIGHT)
             self.col=math.ceil(self.x/RECT_WIDTH)
            else:
                self.row=math.floor(self.y/RECT_HEIGHT)
                self.col=math.floor(self.x/RECT_WIDTH)
           
     def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]
        self.canvas.move(self.id, *delta)   

if __name__ == "__main__":
    Game()