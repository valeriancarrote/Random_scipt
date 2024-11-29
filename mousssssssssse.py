import pyautogui
import random
import time
import pygetwindow as gw

class OtherFunctions:

    @staticmethod
    def shake_mouse():
        offset = 20
        while True:
            currentX, currentY = pyautogui.position()
            x = random.randint(currentX - offset, currentX + offset)
            y = random.randint(currentY - offset, currentY + offset)
            pyautogui.moveTo(x, y)
            time.sleep(0.01)

    @staticmethod
    def window_shaker():
        time.sleep(2)
        win = gw.getActiveWindow()
        if win:
            offset = 2
            for _ in range(1000000000):
                currentX, currentY = win.topleft
                x = random.randint(currentX - offset, currentX + offset)
                y = random.randint(currentY - offset, currentY + offset)
                win.moveTo(x, y)
                time.sleep(0.01)

# Example usage:
# Shake the mouse (commented out to avoid an infinite loop during testing)
# OtherFunctions.shake_mouse()

# Shake the active window
OtherFunctions.window_shaker()
