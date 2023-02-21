# 40. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import platform

mode = platform.architecture()[0] 
if mode.startswith('64'):
    print(f"Python Shell runs on {mode}.")
else:
    print(f"Python Shell does not run on {mode}.")