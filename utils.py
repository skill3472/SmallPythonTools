import datetime


class SimpleFile:
    def __init__(self, name, mtime):
        self.name = name
        self.mtime = mtime
        self.age = datetime.datetime.now().second - mtime

    def __str__(self):
        return self.name