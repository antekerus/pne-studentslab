from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5
gene = "FRAT1"

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "localhost"
PORT = 8080

c = Client(IP, PORT)
print(c)
s = Seq()
filename = "../P00/sequences/" + gene + ".txt"
s.read_fasta(filename)
print("Gene FRAT1:", s)
message = f"Sending {gene} Gene to the server, in fragments of 10 bases..."
response = c.talk(message)

start = 0
stop = 10
i = 1
for fragments in range(i, 5):
    fragment = str(s)[start:stop]
    message = f"Fragment {i}: {fragment}"
    print(message)
    response = c.talk(message)
    start += stop
    stop += stop + 10

