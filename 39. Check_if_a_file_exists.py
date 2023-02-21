# 39. Write a Python program to check whether a file exists.

import os

if os.path.exists("Testing.html"):
    print("File Exists.")
else:
    print("File not Found.")