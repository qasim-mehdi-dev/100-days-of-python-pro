import time
import pyautogui
from PIL import ImageGrab

pyautogui.FAILSAFE = True
DETECTION_ZONE = (720, 525, 760, 535)
 
def check_obstacle_zone(night_mode=False):          
    image = ImageGrab.grab(bbox=DETECTION_ZONE)             
    gray_image = image.convert("L")
    pixels = gray_image.getdata()

    for pixel in pixels:
        if not night_mode and pixel < 100:
            return True
        if night_mode and pixel > 200:
            return True
    return False
        
if __name__ == "__main__":
    print("--- DINO BOT READY ---")
    print("Click inside your Chrome window on the right now...")
    time.sleep(4)

    test_snapshot = ImageGrab.grab(bbox=DETECTION_ZONE)
    test_snapshot.save("dino_test.png")

    print("Bot Active! Pressing Space to start.")
    pyautogui.press("space")
    
    while True:
        if check_obstacle_zone():
            pyautogui.press("space")
            print("Jumped!")
            time.sleep(0.22)  
        
        time.sleep(0.01) 