from Client0 import Client
from Seq1 import Seq1
import os

GENES = ['GENE U5', 'GENE FRAT1', 'GENE ADA', 'GENE FXN', 'GENE RNU6_269P']

PRACTICE = 3
EXERCISE = 7
IP = "localhost"
PORT = 8081

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
c = Client(IP, PORT)
print(c)
bases = ""

print("*Testing PING...")
response = c.talk("PING")
print(response)

print("*Testing GET...")
for n in range(5):
    response = c.talk(f"GET {n}")
    if n == 0:
        bases = response[:-1]
    print(f"GET {n}: {response}")

#bases = c.talk("GET 0")

print("*Testing INFO...")
response = c.talk(f"INFO {bases}")
print(response)

print("*Testing COMP...")
response = c.talk(f"COMP {bases}")
print(response)

print("*Testing REV...")
response = c.talk(f"REV {bases}")
print(response)

print("*Testing GENE...")
i = 0
while i < len(GENES):
    response = c.talk(GENES[i])
    print(GENES[i] + " " + response)
    i += 1