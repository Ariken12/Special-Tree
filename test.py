from TreeScreen import TreeScreen
import tkinter as tk 

root = tk.Tk()
canvas = TreeScreen(root, width=500, height=500)
canvas.pack()
root.after_idle(message)
root.mainloop()