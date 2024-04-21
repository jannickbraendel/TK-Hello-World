#!/usr/bin/env
# -*- coding: utf-8 -*-
from functools import partial
from tkinter import *

window = Tk()
window.geometry('250x300')

languageLabel = Label(window, text='Please select a language.', fg='#F6A800', font='Helvetica')
languageLabel.grid(row=0, sticky='nsew')


# displays greeting in chosen language to the language Label
def greet(lang):
    greeting = ""
    if lang == 'Deutsch':
        greeting = 'Guten Tag!'
    if lang == 'English':
        greeting = 'Hello!'
    if lang == 'French':
        greeting = 'Bonjour!'

    languageLabel.config(text=greeting)


#insert your code here
dButton = Button(window, text='Deutsch', fg='black', command=partial(greet, 'Deutsch'))
dButton.grid(column=0, row=1, sticky='nsew')

eButton = Button(window, text='English', fg='black', command=partial(greet, 'English'))
eButton.grid(column=0, row=2, sticky='nsew')

fButton = Button(window, text='French', fg='black', command=partial(greet, 'French'))
fButton.grid(column=0, row=3, sticky='nsew')

window.columnconfigure(0, weight=1)
window.mainloop()
