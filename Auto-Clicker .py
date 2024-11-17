import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import tkinter as tk
from tkinter import ttk

#input key to activate Auto Clicker
TOGGLE_KEY = KeyCode(char="t")

clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

window = tk() #instantiate an instance of a window
window.geometry("1000x1000")
window.title("Auto Clicker")


window.mainloop()
