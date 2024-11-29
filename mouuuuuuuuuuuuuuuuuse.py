import pyautogui
import random
import time

class MouseShaker:

    @staticmethod
    def shake_mouse():
        offset = 30  # Offset range for the shaking
        while True:
            currentX, currentY = pyautogui.position()  # Get the current mouse position
            x = random.randint(currentX - offset, currentX + offset)  # Generate a random X coordinate within the offset range
            y = random.randint(currentY - offset, currentY + offset)  # Generate a random Y coordinate within the offset range
            pyautogui.moveTo(x, y)  
            time.sleep(0.001) 

MouseShaker.shake_mouse()
