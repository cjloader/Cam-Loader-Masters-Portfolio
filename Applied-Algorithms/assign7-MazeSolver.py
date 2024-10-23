#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog

class Block:
    WALL = 0
    START = 1
    FINISH = 2
    OPEN = 3

class MazeSolver:
    def __init__(self, maze, starting_location):
        self.maze = maze
        self.map = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        self.current_location = starting_location
        self.agenda = []

    def step(self):
        self.map[self.current_location[0]][self.current_location[1]] = 1
        
        # Check the four possible directions
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Up, Left, Down, Right
        for dx, dy in directions:
            new_x = self.current_location[0] + dx
            new_y = self.current_location[1] + dy
            
            if (0 <= new_x < len(self.maze) and
                0 <= new_y < len(self.maze[0]) and
                (self.maze[new_x][new_y] == Block.OPEN or
                 self.maze[new_x][new_y] == Block.FINISH) and
                self.map[new_x][new_y] == 0):
                
                self.agenda.append((new_x, new_y))  # Use tuple instead of list

        if self.agenda:
            self.current_location = self.agenda.pop()
            if self.maze[self.current_location[0]][self.current_location[1]] == Block.FINISH:
                return 1  # Found the finish
            else:
                return 0  # Continue searching
        else:
            return 2  # No more moves possible

class MazeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maze Solver GUI")
        
        self.btn_load = tk.Button(self, text="Load", command=self.load_maze)
        self.btn_load.pack(pady=20)

        self.toggle_button = tk.Button(self, text="Toggle Button")  
        self.toggle_button.pack(pady=20)

        self.text_field = tk.Entry(self)
        self.text_field.pack(pady=20)

        self.canvas = tk.Canvas(self, borderwidth=2, relief="solid")
        self.canvas.pack()

        self.maze = None
        self.starting_location = None

    def load_maze(self):
        maze_data = self.load_from_file()
        if maze_data:
            self.maze = maze_data[0]
            self.starting_location = maze_data[1]
            self.draw_maze()

    def load_from_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return None

        maze = []
        starting_location = None

        with open(file_path, 'r') as file:
            width, height = map(int, file.readline().strip().split())
            for i in range(height):
                line = file.readline().strip()
                row = []
                for j in range(width):
                    char = line[j]
                    if char == '#':
                        row.append(Block.WALL)
                    elif char == '.':
                        row.append(Block.OPEN)
                    elif char == 'o':
                        row.append(Block.START)
                        starting_location = (j, height - 1 - i)
                    elif char == '*':
                        row.append(Block.FINISH)
                maze.append(row)

        return maze, starting_location

    def draw_maze(self):
        self.canvas.delete("all")
        cell_size = 30
        for i, row in enumerate(self.maze):
            for j, block in enumerate(row):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                color = self.get_block_color(block)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def get_block_color(self, block):
        if block == Block.WALL:
            return "black"
        elif block == Block.OPEN:
            return "white"
        elif block == Block.START:
            return "green"
        elif block == Block.FINISH:
            return "red"
        return "gray"  # Default color for unexpected values

if __name__ == "__main__":
    app = MazeGUI()