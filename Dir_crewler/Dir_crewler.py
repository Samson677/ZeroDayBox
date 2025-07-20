import os
import sys

def dir_crawler(path="."):
    filenames = ["dirs.txt", "files.txt"]
    file_handlers = {}

    # Open both files in append mode with utf-8 encoding and store their handlers in a dictionary
    for name in filenames:
        file_handlers[name] = open(name, "a", encoding="utf-8", errors="ignore")

    # Start crawling directories and writing
    for root, dirs, files in os.walk(path):
        for d in dirs:
            file_handlers["dirs.txt"].write(os.path.join(root, d) + "\n")
        for f in files:
            file_handlers["files.txt"].write(os.path.join(root, f) + "\n")

    # Close all files
    for f in file_handlers.values():
        f.close()

if len(sys.argv) < 2:
    path = "."
else:
    path = sys.argv[1]

dir_crawler(path)
