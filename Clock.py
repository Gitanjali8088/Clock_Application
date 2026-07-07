from tkinter import *
from time import strftime

root = Tk()

root.geometry("900x400")
root.configure(bg="#0f172a")
root.resizable(False, False)

colors = [
    "#00FFFF", "#FF00FF", "#00FF00",
    "#FFD700", "#FF4500", "#00BFFF"
]

color_index = 0

def update_clock():
    global color_index

    time_string = strftime("%I:%M:%S %p")
    date_string = strftime("%A, %d %B %Y")

    time_label.config(
        text=time_string,
        fg=colors[color_index]
    )

    date_label.config(text=date_string)

    color_index = (color_index + 1) % len(colors)

    root.after(1000, update_clock)

# Header
title = Label(
    root,
    
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=20)

# Clock Frame
frame = Frame(
    root,
    bg="#1e293b",
    bd=5,
    relief=RIDGE
)
frame.pack(pady=20)

# Time
time_label = Label(
    frame,
    font=("Consolas", 60, "bold"),
    bg="#1e293b"
)
time_label.pack(padx=30, pady=20)

# Date
date_label = Label(
    root,
    font=("Arial", 20),
    bg="#0f172a",
    fg="white"
)
date_label.pack()

# Footer
footer = Label(
    root,

    font=("Arial", 12),
    bg="#0f172a",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=10)

update_clock()

root.mainloop()