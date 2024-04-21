#!/usr/bin/env
# -*- coding: utf-8 -*-

def greet():
    outputStr = ("Select one of the following:\n   [D]eutsch\n   [E]nglish\n   [F]rancais\n[Q]uit\nPlease select: ")
    userInput = input(outputStr)
    if userInput == "D" or userInput == "d":
        print("Guten Tag")
    elif userInput == "E" or userInput == "e":
        print("Hello")
    elif userInput == "F" or userInput == "f":
        print("Bonjour")
    elif userInput == "Q" or userInput == "q":
        print("Quitting...")
    else:
        greet()

greet()