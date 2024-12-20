from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame 
from pygame import mixer
mixer.init()
"""
root = Tk()
root.geometry("1920x1080")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("welcome.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("start.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1905,1060))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.01)
    root.destroy()

play_gif()
root.mainloop()"""
from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk, ImageSequence  # pip install Pillow
import pygame  # pip install pygame
from pygame import mixer

# Initialize pygame mixer
mixer.init()

# Create the root window
root = Tk()
root.geometry("2000x900")

def play_gif():
    """Function to play GIF and audio."""
    # Load the GIF and audio
    gif_path = "welcome.gif"
    audio_path = "start.mp3"
    gif = Image.open(gif_path)
    
    # Play audio
    mixer.music.load(audio_path)
    mixer.music.play()

    # Display GIF frames in a loop
    lbl = Label(root)
    lbl.place(x=0, y=0)

    def update_frame(frame_iter):
        try:
            frame = next(frame_iter)
            frame = frame.resize((2000, 1060))
            img = ImageTk.PhotoImage(frame)
            lbl.config(image=img)
            lbl.image = img  # Keep reference to avoid garbage collection
            root.after(15, update_frame, frame_iter)
            
        except StopIteration:
            root.destroy()

    frame_iter = ImageSequence.Iterator(gif)
    update_frame(frame_iter)

    # Ensure the window stays on top
    root.lift()
    root.attributes("-topmost", True)

# Start playing GIF
play_gif()

# Start the main loop
root.mainloop()

# Cleanup resources
mixer.quit()
