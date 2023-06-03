#// Create a text file in python ? 

n=2
with open("SampleFile.txt", "a") as file:
    file.write('Saving using Python 3 '.format(n))
    file.write( "\n")

#'r' open for reading (default)
#'w' open for writing, truncating the file first
#'x' open for exclusive creation, failing if the file already exists
#'a' open for writing, appending to the end of the file if it exists

