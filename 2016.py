import tkinter as tk
import math
import random as rd


OUTLINE_COLOR = "#BBADA0"
BACKGROUND_COLOR = "#FAF8EF"
FONT_COLOR = "#2D230E"
FONT = ("Arial", 40, "bold")

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
WIDTH, HEIGHT = CANVAS_WIDTH, CANVAS_HEIGHT
ROWS, COLS = 4,4
RECT_WIDTH = CANVAS_WIDTH // COLS
RECT_HEIGHT = CANVAS_HEIGHT // ROWS
MOVE_VEL = RECT_WIDTH  

FPS = 60
racine=tk.Tk()
racine.title("2048")
canevas=tk.Canvas(racine, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")

occupied_positions=set()

def square():
    empty_cells=[(row,col) for row in range(ROWS) for col in range(COLS) if grid[row][col]==0]
    
    if empty_cells:
        row,col=rd.choice(empty_cells)
        grid[row][col]=2
        update_canevas()
    
   
def move_left():
    moved = False
    for row in range(ROWS):
        new_row = [tile for tile in grid[row] if tile != 0]

        i = 0
        while i < len(new_row) - 1:
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                del new_row[i + 1]
                new_row.append(0)
                moved = True
            i += 1
        
        new_row += [0] * (COLS - len(new_row))

        if grid[row] != new_row:
            grid[row] = new_row
            moved = True
    if moved:
        square()
        update_canevas()

grid = [[0] * COLS for _ in range(ROWS)]    
def update_canevas():
    canevas.delete("all")
    draw_grid()
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] != 0:
                x0, y0 = col * RECT_WIDTH, row * RECT_HEIGHT
                x1, y1 = x0 + RECT_WIDTH, y0 + RECT_HEIGHT
                canevas.create_rectangle(x0, y0, x1, y1, fill="blue")
                canevas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=str(grid[row][col]), font=("arial", 50), fill="white")

def draw_grid():   
    canevas.create_line(CANVAS_WIDTH/4,0,CANVAS_WIDTH/4,CANVAS_HEIGHT)
    canevas.create_line(CANVAS_WIDTH/2,0,CANVAS_WIDTH/2,CANVAS_HEIGHT)
    canevas.create_line(CANVAS_WIDTH*0.75,0,CANVAS_WIDTH*0.75,CANVAS_HEIGHT)
    canevas.create_line(0,CANVAS_HEIGHT/4,CANVAS_WIDTH,CANVAS_HEIGHT/4)
    canevas.create_line(0,CANVAS_HEIGHT/2,CANVAS_WIDTH,CANVAS_HEIGHT/2)
    canevas.create_line(0,CANVAS_HEIGHT*0.75,CANVAS_WIDTH,CANVAS_HEIGHT*0.75)
left=tk.Button(racine,text="left",command=move_left)
carre=tk.Button(racine,text="carre",command=square)
grid_button=tk.Button(racine,text="lines",command=draw_grid)
carre.grid(row=0,column=2)
canevas.grid(row=0,column=0)
grid_button.grid(row=0,column=1)
left.grid(row=0,column=3)


racine.mainloop()

