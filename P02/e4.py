from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4
genes = ["U5", "ADA", "FRAT1"]

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "localhost"
PORT = 8080

c = Client(IP, PORT)
print(c)
s = Seq()
for gene in genes:
    filename = "../P00/sequences/" + gene + ".txt"
    s.read_fasta(filename)
    message = f"Sending {gene} Gene to the server..."
    print(f"To Server: {message}")
    response = c.talk(message)
    print("From Server: \n \n")
    print(response)
    print(f"To Server: {s}")
    response = c.talk(str(s))
    print("From Server:\n \n")
    print(response)


