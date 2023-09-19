from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")
        with open("data.txt", "a") as file:
            file.write(f"{x}, {y}\n")

while True:
    # Create a listener for mouse events
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()