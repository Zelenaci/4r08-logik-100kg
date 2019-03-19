#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:42:26 2018

@author: svo35103
"""

import tkinter as tk

BARVY = "#c90000 #99dd00 #0000ff #ffff00 #008888 #880088 #dd9900 #ffffff".split()
BTN_W = 30
BTN_H = 20

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.gui()
        #self.tlacbarvy()
        #self.level = 1
        
    def gui(self):
        offset = 0
        
        # HORNI POLE SKRYTYCH BAREV
        self.canvases_1 = []
        for x in range(5):
            canvas = tk.Canvas(self.master, background="black", width=BTN_W, height=BTN_H)
            canvas.grid(column=x, row=offset)
            self.canvases_1.append(canvas)
        offset += 1
        
        # NAPIS LOGIK
        self.napislogik = tk.Label(self.master, text="Logik")
        self.napislogik.grid(column=0, row=offset, columnspan=5)
        offset += 1
        
        # HORNI POLE VYBRANYCH VOLEB
        self.canvases_2 = []
        self.scorecan_2 = []
        for y in range(10):
            self.canvases_2.append([])
            for x in range(5):
                canvas = tk.Canvas(self.master, background="gray", width=BTN_W, height=BTN_H)
                canvas.grid(column=x, row=offset)
                self.canvases_1.append(canvas)
            score = tk.Label(self.master, text="  -/-  ")
            score.grid(column=5, row=offset)
            offset += 1
            
        # NAPIS PALETA
        self.napispaleta = tk.Label(self.master, text="Paleta")
        self.napispaleta.grid(column=0, row=offset, columnspan=5)
        
        # TLACITKO ODESLAT
        sendbut = tk.Button(self.master, text="Odeslat", command=self.kontrola)
        sendbut.grid(column=5, row=offset)
        offset += 1
        
        # SPODNI POLE BAREV
        self.buttons_3 = []
        for y, barva in enumerate(BARVY):
            self.buttons_3.append([])
            for x in range(5):
                button = tk.Button(self.master, background=barva, image=PIXEL, width=BTN_W, 
                                   height=BTN_H, command=lambda: self.zmacknutiBarvy(y, x, barva))
                button.grid(column=x, row=offset)
                self.button_3.append(button)
            offset += 1
        
        pass
    
    def kontrola(self):
        pass
    
    def tlacBarvy(self, x, y):
        tlacitka = []
        for a in range(y):
            tlacitka.append([])
            for b in range(x):
                pass
                # udelej neco
                
    def zmacknutiBarvy(self, *args):
        pass
    
    def confirm(self):
        pass
        self.level += 1
    
master = tk.Tk()
PIXEL = tk.PhotoImage(width=1, height=1)
app = Application(master)
app.mainloop()