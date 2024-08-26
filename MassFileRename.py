#!/usr/bin/env python3
import os
import argparse
import datetime
from string import ascii_uppercase
from utils import SimpleFile

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Parent directory to rename files in.", type=str)
parser.add_argument("-s", "--sortby", help="Determine the order of files.", choices=["dateOldFirst", "dateNewFirst", "AtoZ", "ZtoA"], type=str, default="dateOldFirst", required=False)
parser.add_argument("-n", "--namingmode", help="New naming convention.", choices=["AtoZ", "123"], type=str, default="123", required=False)
args = parser.parse_args()


def sortByName(InArray, Reversed) -> list[str]:
    return sorted(InArray, reverse=Reversed, key=str.lower)


def sortByDate(InArray, OldestFirst) -> list[str]:
    SFileArray = []
    for file in InArray:
        mtime = os.path.getmtime(f"{args.directory}/{file}")
        SFileArray.append(SimpleFile(file, mtime))
    SFileArray = sorted(SFileArray, key=lambda x: x.age, reverse=OldestFirst)
    OutArray = [x.name for x in SFileArray]
    return OutArray


def numToLetter(n) -> str:
    letters = ascii_uppercase
    res = ''
    while n > 0:
        n -= 1
        res = letters[n % len(letters)] + res
        n //= 26

    return res

files = os.listdir(args.directory)
if args.sortby == "dateOldFirst":
    files = sortByDate(files, True)
elif args.sortby == "dateNewFirst":
    files = sortByDate(files, False)
elif args.sortby == "AtoZ":
    files = sortByName(files, False)
else:
    files = sortByName(files, True)

for i in range(1, len(files)):
    extension = os.path.splitext(files[i])[1]
    if args.namingmode == "AtoZ":
        newName = numToLetter(i) + extension
    else:
        newName = str(i) + extension

    try:
        os.rename(f"{args.directory}/{files[i]}", f"{args.directory}/{newName}")
    except FileExistsError:
        print(f"Cannot rename {files[i]} to {newName} - file name, already taken.")
        continue
    print(f"Changing {files[i]} to {newName}...")

print("Done!")