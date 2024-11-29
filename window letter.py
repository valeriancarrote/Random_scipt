import tkinter as tk
import keyboard
import random

def create_new_window(letter):
    x = random.randint(0, root.winfo_screenwidth() - 100)
    y = random.randint(0, root.winfo_screenheight() - 100)
    
    new_window = tk.Toplevel(root)
    new_window.geometry(f"100x100+{x}+{y}")
    #new_window.overrideredirect(True)
    
    letter_label = tk.Label(new_window, text=letter, font=("Arial", 50), fg="black")
    letter_label.pack()


    letter_label.configure(bg=new_window['bg'], highlightthickness=0)

def on_key_press(event):
    if event.name.isalpha():
        letter = event.name
        print(letter)
        create_new_window(letter)
    elif event.name == 'right ctrl':
        for window in root.winfo_children():
            if isinstance(window, tk.Toplevel):
                window.destroy()

root = tk.Tk()
root.geometry("40x140")


keyboard.on_press(on_key_press)

root.mainloop()
