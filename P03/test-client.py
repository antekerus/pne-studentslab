from Client0 import Client

PRACTICE = 3
EXERCISE = 7
IP = "localhost"
PORT = 8080
GENES = ["GENE U5", "GENE ADA", "GENE FRAT1", "GENE FXN", "GENE RNU6_269P"]

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
c = Client(IP, PORT)
print(c)

print("* Testing PING...")
response = c.talk("PING")
print(response)

print("* Testing GET...")
for n in range(5):
    response = c.talk(f"GET {n}")
    if n == 0:
        bases = response[:-1]
    print(f"GET {n}: {response}")

print("* Testing INFO...")
response = c.talk(f"INFO {bases}")
print(response)

print("* Testing COMP...")
response = c.talk(f"COMP {bases}")
print("COMP", response)

print("* Testing REV...")
response = c.talk(f"REV {bases}")
print("REV", response)

print("* Testing GENE...")
i = 0
while i < len(GENES):
    response = c.talk(GENES[i])
    print(GENES[i] + " " + response)
    i += 1
