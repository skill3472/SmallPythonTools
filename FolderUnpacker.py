#!/usr/bin/env python3
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Parent directory to unpack subdirs from.", type=str)
args = parser.parse_args()

PARENT_DIR = args.directory
walk = os.walk(PARENT_DIR)
dirArr = []
for path, dirs, files in walk:
    if dirs not in dirArr and dirs:
        dirArr.append(dirs)

try:
    dirArr = dirArr[0]
except IndexError:
    print("Directory not found!")
    exit(1)

for directory in dirArr:
    files = os.listdir(f"{PARENT_DIR}/{directory}")
    if len(files) > 1:
        print(f'Couldn\'t move file from {directory} - multiple files found!')
        continue
    elif len(files) == 1:
        file = files[0]
        file_ext = os.path.splitext(file)[1]
        os.rename(f"{PARENT_DIR}/{directory}/{file}", f"{PARENT_DIR}/{directory}{file_ext}")
        os.rmdir(f"{PARENT_DIR}/{directory}")
    else:
        print(f'Couldn\'t move file from {directory} - no files found!')
        continue

print('Done moving files!')