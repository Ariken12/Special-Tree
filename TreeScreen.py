import tkinter as tk
from tkinter import messagebox
from functions import save_in_word, random_color
from PIL import Image
import math
import subprocess
import os

COEFFICIENT = 4

class TreeScreen(tk.Frame):
    def __init__(self, *args, width=500, height=500, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height
        self.angle = 40
        self.center = (width//2, height//2)
        self.dots = []
        self.tan = math.tan(math.radians(90 - self.angle / 2)) 
        self.upview = tk.Canvas(self, width=width, height=height)
        self.sideview_front = tk.Canvas(self, width=width, height=(width//2)*self.tan)
        self.sideview_back = tk.Canvas(self, width=width, height=(width//2)*self.tan)
        self.upview.create_oval(2, 2, width, height)
        self.sideview_front.create_polygon((0, (width//2)*self.tan), (width//2, 0), (width, (width//2)*self.tan), fill='', outline='black')
        self.sideview_back.create_polygon((0, (width//2)*self.tan), (width//2, 0), (width, (width//2)*self.tan), fill='', outline='black')
        self.button_save = tk.Button(self, text='Сохранить', command=self.save)
        self.button_clear = tk.Button(self, text='Очистить', command=self.clear)
        self.upview.bind('<Button-1>', self.add_dots)
        self.upview.pack(side='top')
        self.sideview_front.pack(side='left')
        self.sideview_back.pack(side='right')
        self.button_save.pack()
        self.button_clear.pack()

    def add_dots(self, event):
        x = event.x
        y = event.y
        radius = ((x - self.center[0]) ** 2 + (y - self.center[0]) ** 2) ** 0.5
        if radius > self.center[0]:
            return 
        lenght = radius * self.tan
        self.upview.create_oval(x-2, y-2, x+2, y+2, fill=random_color(), outline='')
        if y > self.center[1]:
            self.sideview_front.create_oval(x-2, lenght-2, x+2, lenght+2, fill=random_color(), outline='')
        else:
            self.sideview_back.create_oval(x-2, lenght-2, x+2, lenght+2, fill=random_color(), outline='')
        self.upview.update()
        self.dots.append((x * COEFFISIENT, y * COEFFISIENT, (lenght+radius) * COEFFISIENT, radius * COEFFISIENT))

    def clear(self):
        self.dots = []
        self.upview.delete('all')
        self.sideview_back.delete('all')
        self.sideview_front.delete('all')
        self.upview.create_oval(2, 2, self.width, self.height)
        self.sideview_front.create_polygon((0, (self.width//2)*self.tan), (self.width//2, 0), (self.width, (self.width//2)*self.tan), fill='', outline='black')
        self.sideview_back.create_polygon((0, (self.width//2)*self.tan), (self.width//2, 0), (self.width, (self.width//2)*self.tan), fill='', outline='black')
        self.upview.update()
        self.sideview_back.update()
        self.sideview_front.update()

    def save(self):
        save_in_word(self.dots)