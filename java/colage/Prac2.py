import tkinter as tk
import random
from tkinter import messagebox

class Minesweeper:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")
        
        self.grid_size = 5
        self.mine_count = 5
        self.score = 0
        
        self.create_widgets()
        self.start_game()
    
    def create_widgets(self):
        tk.Label(self.root, text="Grid Size:").grid(row=0, column=0)
        self.grid_entry = tk.Entry(self.root)
        self.grid_entry.grid(row=0, column=1)
        self.grid_entry.insert(0, "5")
        
        tk.Label(self.root, text="Number of Mines:").grid(row=1, column=0)
        self.mine_entry = tk.Entry(self.root)
        self.mine_entry.grid(row=1, column=1)
        self.mine_entry.insert(0, "5")
        
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2)
        
        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.grid(row=3, column=0, columnspan=2)
        
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.grid(row=4, column=0, columnspan=2)
    
    def start_game(self):
        self.grid_size = int(self.grid_entry.get())
        self.mine_count = int(self.mine_entry.get())
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        
        self.mines = set()
        while len(self.mines) < self.mine_count:
            self.mines.add(random.randint(0, self.grid_size * self.grid_size - 1))
        
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        
        self.buttons = []
        for i in range(self.grid_size):
            row_buttons = []
            for j in range(self.grid_size):
                index = i * self.grid_size + j
                btn = tk.Button(self.grid_frame, text="", width=4, height=2,
                                command=lambda idx=index: self.cell_clicked(idx))
                btn.grid(row=i, column=j)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)
    
    def cell_clicked(self, index):
        row, col = divmod(index, self.grid_size)
        if index in self.mines:
            self.buttons[row][col].config(text="X", bg="red")
            messagebox.showinfo("Game Over", f"You hit a mine! Final Score: {self.score}")
            self.root.quit()  # Exit the game when a mine is hit
        else:
            points = random.randint(1, 10)
            self.buttons[row][col].config(text=str(points), bg="green", state=tk.DISABLED)
            self.score += points
            self.score_label.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()
