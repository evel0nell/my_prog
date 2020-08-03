import os
import datetime
import time
from datetime import datetime
import progressbar

import tkinter as tk

from tkinter import simpledialog
from tkinter import ttk
from tqdm import tqdm



def change(file, path):

    local_time = time.ctime(os.path.getmtime(path))
    date = datetime.strptime(local_time, "%a %b %d %H:%M:%S %Y")
    NEW_LINE =date.strftime(("%Y%m%d") +"_" + str(file))
    if str(file).startswith(date.strftime("%Y%m%d")):
        return None

    os.rename(os.path.join(path, file), os.path.join(path, NEW_LINE))

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Name Changer",
                                  prompt="Write the path:")
path = USER_INP
for path, dirs, files in os.walk(path):

    for file in files:
        print(file)


        change(file, path)

#/home/evelina/Documents/TEST7
print("ready")
ROOT.mainloop()

