# Program to automatically create new text file everyday with date stamp in it.

import datetime
import os

# Get the current Date and time

now = datetime.datetime.now()
today = "data" + (now.strftime("%y_%m_%d"))
save_path = 'F:\\test\\'
completeName = os.path.join(save_path, today+".txt")

# This part will check if there is already a file created or not. If created it write in the existing file and close it.

if os.path.exists(today):
    file = open(completeName, "r+")
else:
    file = open(completeName, "w")

file.write("Test write was successful")
file.close()
print(f'Path of the New File Created: {completeName}')
