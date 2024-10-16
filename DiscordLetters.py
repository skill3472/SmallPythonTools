#!/usr/bin/env python3
import string
inputText = input()
outText = ""

for letter in inputText:
    if letter in string.ascii_letters or letter in "?! ":
        if letter == " ":
            outText += "\t"
        elif letter == "?":
            outText += ":question: "
        elif letter == "!":
            outText += ":exclamation: "
        else:
            outText += ":regional_indicator_" + letter.lower() + ": "
    else:
        exit(1)

print(outText)