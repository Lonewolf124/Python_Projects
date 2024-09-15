from tkinter import *
from PIL import Image, ImageTk
import pygame

root = Tk()
root.geometry("1000x1033")
root.title("Messi")

# Load the image using PIL (Pillow)
image = Image.open("messi.jpg")

# Resize the image to your desired dimensions
new_width = 400  # Set your desired width
new_height = 300  # Set your desired height
resized_image = image.resize((new_width, new_height))
photo = ImageTk.PhotoImage(resized_image)

image_frame = Frame(root)
image_frame.pack(side=LEFT, fill=BOTH, expand=True)

image_label = Label(image_frame, image=photo)
image_label.pack(fill=BOTH, expand=True)

text_frame = Frame(root)
text_frame.pack(side=LEFT, fill=BOTH, expand=True)

title_text = '''Lionel Andrés Messi; born 24 June 1987), also known as Leo Messi, is an
Argentine professional footballer who plays as a forward for and captains both Major
League Soccer club Inter Miami and the Argentina national team. Widely regarded as one of the
greatest players of all time, Messi has won a record eight Ballon d'Or awards and a record six
European Golden Shoes, and in 2020 he was named to the Ballon d'Or Dream Team. Until leaving
the club in 2021, he had spent his entire professional career with Barcelona, where he won
a club-record 34 trophies, including ten La Liga titles, seven Copa del Rey titles and the
UEFA Champions League four times.[note 3] With his country, he won the 2021 Copa
América and the 2022 FIFA World Cup. '''

title_label = Label(text_frame, text=title_text, bg="lightgreen", fg="Crimson", padx=13, pady=9, wraplength=400, font="BAZOOKA 10 bold", borderwidth=5, relief=SUNKEN, justify="center")
title_label.pack(fill=BOTH, expand=True)

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load and play the sound
pygame.mixer.music.load("sound1.mp3")  # Replace "your_sound_file.mp3" with the path to your sound file
pygame.mixer.music.play()

root.mainloop()

# for i in range(-10): 
#     pass 
#     print("hi")

# if 4+6==10: print("TRUE")
# else: print("False") 
# print ("TRUE")