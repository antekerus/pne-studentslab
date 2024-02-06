from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text().split("\n")
file_contents.pop(0)


# -- Print the contents on the console
print(len(''.join(file_contents)))