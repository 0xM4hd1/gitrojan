import os


def run(**args):
    print("dirlist module")
    files = os.listdir(".")
    return str(files)