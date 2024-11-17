import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import tkinter as tk
from tkinter import ttk

# Input key to activate Auto Clicker
TOGGLE_KEY = KeyCode(char="t")

clicking = False
mouse = Controller()


def clicker():
    """Threaded function for performing auto-clicking."""
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)


def toggle_event(key):
    """Toggle auto-clicking using the keyboard key."""
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking
        update_status()


def start_clicking():
    """Start the auto-clicker."""
    global clicking
    clicking = True
    update_status()


def stop_clicking():
    """Stop the auto-clicker."""
    global clicking
    clicking = False
    update_status()


def update_status():
    """Update the status label in the GUI."""
    status = "Activated" if clicking else "Deactivated"
    status_label.config(text=f"Status: {status}")


# Initialize the Tkinter window
window = tk.Tk()
window.geometry("400x200")
window.title("Auto Clicker")

# Set global background color
window.config(bg="black")

#Title for GUI
Title_label = tk.Label(window, text="Auto Clicker", font=("Arial", 16, "bold"),fg="#00FF00",bg="black")
Title_label.pack(pady=10)

# Status Label
status_label = tk.Label(window, text="Status: Deactivated", font=("Arial", 14),fg="#00FF00",bg="black")
status_label.pack(pady=20)

#Key Label
key_label = tk.Label(window, text="Press T to Activate or Deactivate", font=("Arial", 16),fg="#00FF00",bg="black")
key_label.pack(pady=30)

# Run the clicker thread
click_thread = threading.Thread(target=clicker, daemon=True)
click_thread.start()

# Set up the keyboard listener in another thread
def keyboard_listener():
    with Listener(on_press=toggle_event) as listener:
        listener.join()


listener_thread = threading.Thread(target=keyboard_listener, daemon=True)
listener_thread.start()

# Run the Tkinter main loop
window.mainloop()
