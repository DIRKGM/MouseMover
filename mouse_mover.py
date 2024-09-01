import pyautogui
import time
import random
import sys

def move_mouse():
    while True:
        try:
            # Zufällige Bewegung zwischen -100 und 100 Pixeln in x- und y-Richtung
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            
            # Bewege die Maus relativ zur aktuellen Position
            pyautogui.moveRel(x, y, duration=0.5)
            
            # Warte zwischen 30 und 60 Sekunden bis zur nächsten Bewegung
            time.sleep(random.uniform(30, 60))
            
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            time.sleep(5)  # Warte 5 Sekunden bevor es weitergeht

if __name__ == "__main__":
    try:
        print("Mausbeweger gestartet. Drücken Sie Strg+C, um das Programm zu beenden.")
        move_mouse()
    except KeyboardInterrupt:
        print("\nProgramm wird beendet.")
        sys.exit(0)