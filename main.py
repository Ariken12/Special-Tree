from TreeScreen import TreeScreen
import tkinter as tk 

WIDTH = 250
HEIGHT = 250

root = tk.Tk()
canvas = TreeScreen(root, width=WIDTH, height=HEIGHT)
canvas.pack()
root.mainloop()