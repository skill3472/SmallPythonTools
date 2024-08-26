## Small Python Tools
is a collection of small tools I've written for my own purposes and use in Python. If you find any of them useful, feel free to use them.
Below, you can find a short description of each tool, which will be updated, if any are added.

## FolderUnpacker.py
is a tool, for *"unpacking"* folders. For ex, this directory structure:
```
Parent Directory/
├─ Name1/
│  ├─ file1.pdf
├─ Name2/
│  ├─ file2.exe
├─ Name3/
│  ├─ file3.mp3
```
after using this tool, with the path to "Parent Directory", turns into:
```
Parent Directory/
├─ Name1.pdf
├─ Name2.exe
├─ Name3.mp3
```

## MassFileRename.py
is a tool for renaming files based on sorting by name/date. For example:
```
Parent Directory/
├─ John.pdf -> 2.pdf
├─ Leah.pdf -> 3.pdf
├─ Abel.pdf -> 1.pdf
```
or even
```
Parent Directory/
├─ John.pdf -> B.pdf
├─ Leah.pdf -> C.pdf
├─ Abel.pdf -> A.pdf
```