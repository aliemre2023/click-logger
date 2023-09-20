from pynput import mouse
import time

start = time.time()

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")
        current = time.time() - start
        with open("data.txt", "a") as file:
            file.write(f"{x}, {y}, {round(current, 3)}\n")

while True:
    # Create a listener for mouse events
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()