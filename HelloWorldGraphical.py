#!/usr/bin/env
# -*- coding: utf-8 -*-
from functools import partial
from tkinter import *

window = Tk()
window.geometry('250x300')
window.minsize(250,300)

languageLabel = Label(window, text='Please select a language.', fg='#F6A800', font='Helvetica', justify='center')
languageLabel.grid(row=0, sticky='nsew', padx=10, pady=10)


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


# create one button for each language (same config)
languages = ['Deutsch', 'English', 'French']
for i in range(3):
    button = Button(window, text=languages[i], fg='black', command=partial(greet, languages[i]), justify='center',
                    font='Helvetica 12', borderwidth=3)
    button.grid(column=0, row=i + 1, sticky='nsew', padx=10, pady=10)

quitButton = Button(window, text='Quit', fg='black', command=window.quit, justify='center', font='Helvetica 10')
quitButton.grid(column=0, row=4, sticky='nse', padx=(70, 10), pady=(50, 10))

# columns and rows are adjusted when window size is changed
window.columnconfigure(0, weight=1)
for i in range(5):
    window.rowconfigure(i, weight=1)
window.mainloop()
