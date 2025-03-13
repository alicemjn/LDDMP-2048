import tkinter as tk
import math
import random

# Game constants
FPS = 60
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4
RECT_WIDTH, RECT_HEIGHT = WIDTH // COLS, HEIGHT // ROWS

OUTLINE_COLOR = "#BBADA0"
BACKGROUND_COLOR = "#FAF8EF"
FONT_COLOR = "#2D230E"
FONT = ("Arial", 40, "bold")

MOVE_VEL = RECT_WIDTH  # Move by one tile size


class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048")
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
        self.canvas.pack()

        self.tiles = {}  # Stores tiles in dictionary with "row,col" as keys
        self.draw_grid()
        self.generate_tiles()
        
        # Key bindings for movement
        self.window.bind("<Left>", lambda event: self.move_tiles("left"))
        self.window.bind("<Right>", lambda event: self.move_tiles("right"))
        self.window.bind("<Up>", lambda event: self.move_tiles("up"))
        self.window.bind("<Down>", lambda event: self.move_tiles("down"))

        self.window.mainloop()

    def draw_grid(self):
        """Draws the 4x4 grid."""
        for row in range(1, ROWS):
            y = row * RECT_HEIGHT
            self.canvas.create_line(0, y, WIDTH, y, fill=OUTLINE_COLOR, width=5)

        for col in range(1, COLS):
            x = col * RECT_WIDTH
            self.canvas.create_line(x, 0, x, HEIGHT, fill=OUTLINE_COLOR, width=5)

    def generate_tiles(self):
        """Creates two random tiles at the beginning."""
        for _ in range(2):
            self.add_random_tile()

    def add_random_tile(self):
        """Adds a random tile with value 2 or 4 in an empty spot."""
        if len(self.tiles) >= ROWS * COLS:
            return  # No space to add new tiles

        while True:
            row, col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
            if f"{row},{col}" not in self.tiles:
                self.tiles[f"{row},{col}"] = Tile(self.canvas, row, col, random.choice([2, 4]))
                break

    def move_tiles(self, direction):
        """Handles tile movement based on user input (left, right, up, down)."""
        moved = False
        merged_positions = set()

        sorted_tiles = sorted(self.tiles.values(), key=lambda tile: (tile.row, tile.col), reverse=(direction in ["right", "down"]))

        for tile in sorted_tiles:
            old_pos = (tile.row, tile.col)

            while True:
                new_row, new_col = tile.row, tile.col
                if direction == "left":
                    new_col -= 1
                elif direction == "right":
                    new_col += 1
                elif direction == "up":
                    new_row -= 1
                elif direction == "down":
                    new_row += 1

                if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                    break  # Stop if it reaches the boundary

                next_tile = self.tiles.get(f"{new_row},{new_col}")

                if next_tile is None:  
                    tile.row, tile.col = new_row, new_col  # Move tile
                    moved = True
                elif next_tile.value == tile.value and (new_row, new_col) not in merged_positions:
                    next_tile.value *= 2  # Merge tiles
                    tile.delete()
                    del self.tiles[f"{old_pos[0]},{old_pos[1]}"]
                    merged_positions.add((new_row, new_col))
                    moved = True
                    break
                else:
                    break  # Stop moving if a different tile is blocking the way

        if moved:
            self.add_random_tile()
            self.redraw_tiles()

        if self.check_game_over():
            print("Game Over!")

    def redraw_tiles(self):
        """Clears and redraws all tiles."""
        self.canvas.delete("tile")
        for tile in self.tiles.values():
            tile.draw()

    def check_game_over(self):
        """Checks if the game is lost (no moves left)."""
        if len(self.tiles) < ROWS * COLS:
            return False  # There are empty spaces, so game is not over

        for tile in self.tiles.values():
            row, col = tile.row, tile.col
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = self.tiles.get(f"{row + dr},{col + dc}")
                if neighbor and neighbor.value == tile.value:
                    return False  # Move is possible
        return True  # No moves left


class Tile:
    """Represents a single tile in the 2048 game."""
    COLORS = ["#EEE4DA", "#EDE0C8", "#F2B179", "#F59563", "#F67C5F", "#F65E3B", "#EDCF72",
              "#EDCC61", "#EDC850", "#EDC53F", "#EDC22E", "#3E3933"]

    def __init__(self, canvas, row, col, value):
        self.canvas = canvas
        self.row = row
        self.col = col
        self.value = value

    def draw(self):
        """Draws the tile on the canvas."""
        x1, y1 = self.col * RECT_WIDTH, self.row * RECT_HEIGHT
        x2, y2 = x1 + RECT_WIDTH, y1 + RECT_HEIGHT

        color = self.get_color()
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="tile")
        self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(self.value), font=FONT, tags="tile")

    def get_color(self):
        """Returns the tile's color based on its value."""
        index = int(math.log2(self.value)) - 1
        return Tile.COLORS[index] if 0 <= index < len(Tile.COLORS) else "#3E3933"

    def delete(self):
        """Removes the tile from the canvas."""
        self.canvas.delete("tile")


if __name__ == "__main__":
    Game()
