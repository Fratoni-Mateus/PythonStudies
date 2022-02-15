#  1. Get a list of the file names
#  2. Extract the place names from the file names
#  3. Make a directory for each place names
#  4. Move files into the right directories


import os


os.chdir("Photos")
originals = os.listdir()

print(originals) #  Just for testing the code
