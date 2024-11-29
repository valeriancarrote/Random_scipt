import tkinter as tk
import random as r
import math

u = ["#000000", "#FF0000", "#800080", "#008000", "#FFFF00", "#00FFFF", "#0000FF", "#FF00FF"]

class MovableWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Movable Window")
        self.geometry("50x50")
        self.configure(bg="#ffffff")
        #self.overrideredirect(True)  # Remove window decorations
        self.attributes('-alpha', 0.5)

        self.bind("<KeyPress>", self.move_window)

        self.trainer_window = None  # Reference to the trainer window
        self.apple_window = None  # Reference to the apple window

    def move_window(self, event):
        key = event.keysym
        if key == "Left":
            self.geometry("+{x}+{y}".format(x=self.winfo_x() - 10, y=self.winfo_y()))
        elif key == "Right":
            self.geometry("+{x}+{y}".format(x=self.winfo_x() + 10, y=self.winfo_y()))
        elif key == "Up":
            self.geometry("+{x}+{y}".format(x=self.winfo_x(), y=self.winfo_y() - 10))
        elif key == "Down":
            self.geometry("+{x}+{y}".format(x=self.winfo_x(), y=self.winfo_y() + 10))
        
        if self.apple_window is not None:
            self.check_apple_collision()

    def create_trainer_window(self):
        power = r.choice(u)
        self.trainer_window = tk.Toplevel(self)
        self.trainer_window.title("Trainer Window")
        self.trainer_window.geometry("50x50")
        self.trainer_window.configure(bg=power)
        self.trainer_window.overrideredirect(True)

        # Set the position of the trainer window relative to the original window
        self.trainer_window.geometry("+{x}+{y}".format(x=self.winfo_x() + 50, y=self.winfo_y() + 50))

        self.after(5000, self.trainer_window.destroy)  # Destroy the trainer window after 5 seconds
        self.after(100, self.create_trainer_window)

    def create_apple_window(self):
        self.apple_window = tk.Toplevel(self)
        self.apple_window.title("Apple Window")
        self.apple_window.geometry("50x50")
        self.apple_window.configure(bg="red")
        self.apple_window.overrideredirect(True)

        # Set the position of the apple window at a random location
        x = r.randint(0, self.winfo_screenwidth() - 50)
        y = r.randint(0, self.winfo_screenheight() - 50)
        self.apple_window.geometry("+{x}+{y}".format(x=x, y=y))

        self.after(1000000000, self.apple_window.destroy)  # Destroy the apple window after 10 seconds
        self.after(5000, self.create_apple_window)  # Create a new apple window every 5 seconds

    def check_apple_collision(self):
        apple_x = self.apple_window.winfo_x()
        apple_y = self.apple_window.winfo_y()
        trainer_x = self.winfo_x()
        trainer_y = self.winfo_y()

        distance = math.sqrt((apple_x - trainer_x) ** 2 + (apple_y - trainer_y) ** 2)

        if distance <= 100:
            self.apple_window.destroy()
            self.apple_window = None
            print("Apple eaten!")

window = MovableWindow()
window.create_trainer_window()
window.create_apple_window()  # Create the initial apple window
window.mainloop()