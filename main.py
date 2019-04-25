#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:42:26 2018

@author: svo35103
"""

import tkinter as tk
from functools import partial
from random import choice

BARVY = "#c90000 #99dd00 #0000ff #ffff00 #008888 #880088 #dd9900 #ffffff".split()
BTN_W = 30
BTN_H = 20

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.gui()
        self.kod = self.randomhadanka()
        self.level = 1
        self.status = True

    def gui(self):
        offset = 0

        # HORNI POLE SKRYTYCH BAREV
        self.canvases_1 = []
        for x in range(5):
            canvas = tk.Canvas(self.master, background="black", width=BTN_W, height=BTN_H)
            self.canvases_1.append(canvas)
            self.canvases_1[x].grid(column=x, row=offset)
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
                self.canvases_2[y].append(canvas)
                self.canvases_2[y][x].grid(column=x, row=offset)
            score = tk.Label(self.master, text="  -/-  ")
            self.scorecan_2.append(score)
            self.scorecan_2[y].grid(column=5, row=offset)
            offset += 1

        # NAPIS PALETA
        self.napispaleta = tk.Label(self.master, text="Paleta")
        self.napispaleta.grid(column=0, row=offset, columnspan=5)

        # TLACITKO ODESLAT
        self.sendbut = tk.Button(self.master, text="Odeslat", command=self.kontrola)
        self.sendbut.grid(column=5, row=offset)
        offset += 1

        # SPODNI POLE BAREV
        self.buttons_3 = []
        for y, barva in enumerate(BARVY):
            self.buttons_3.append([])
            for x in range(5):
                akce = partial(self.zmacknutiBarvy, x, y, barva)
                button = tk.Button(self.master, background=barva, image=PIXEL, width=BTN_W,
                                   height=BTN_H, command=akce)
                self.buttons_3[y].append(button)
                self.buttons_3[y][x].grid(column=x, row=offset)
            offset += 1

    def randomhadanka(self):
        hadanka = []
        barvy = BARVY
        for _ in range(5):
            barva = choice(barvy)
            hadanka.append(barva)
            barvy.remove(barva)
        return hadanka

    def konec(self):
        for x in range(5):
            self.canvases_1[x].configure(bg=self.kod[x])
        self.status = False

    def kontrola(self):
        line = 10 - self.level
        spravnemisto = 0
        spravnabarva = 0
        for x in range(5):
            barva = self.canvases_2[line][x].config()["background"][-1]
            if barva in self.kod:
                spravnabarva += 1
            if barva == self.kod[x]:
                spravnemisto += 1
        self.scorecan_2[line].configure(text="{} / {}".format(spravnemisto, spravnabarva))
        if self.level == 10:
            self.konec()
        self.level += 1
        if spravnemisto == 5:
            self.konec()

    def zmacknutiBarvy(self, x, y, barva):
        if not(self.status):
            return
        line = 10 - self.level
        self.canvases_2[line][x].configure(bg=barva)

master = tk.Tk()
PIXEL = tk.PhotoImage(width=1, height=1)
app = Application(master)
app.mainloop()
