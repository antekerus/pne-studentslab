from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()
first_line_i = file_contents.find("\n")
sequence = file_contents[first_line_i:]
sequence = sequence.replace("\n", "")

# -- Print the contents on the console
print(sequence)