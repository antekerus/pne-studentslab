from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6
gene = "FRAT1"

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "localhost"
PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
print(c1)
c2 = Client(IP, PORT2)
print(c2)
s = Seq()
filename = "../P00/sequences/" + gene + ".txt"
s.read_fasta(filename)
print("Gene FRAT1:", s)
message = f"Sending {gene} Gene to the server, in fragments of 10 bases..."
response = c1.talk(message)

n = 0
i = 0
while n < 10:
    fragment = str(s)[i:i+10]
    message = f"Fragment {n + 1}: {fragment}"
    print(message)
    if n % 2 == 0:
        response = c2.talk(message)
    else:
        response = c1.talk(message)
    n += 1
    i += 10