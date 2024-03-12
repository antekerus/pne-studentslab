from Client0 import Client

PRACTICE = 3
EXERCISE = 7
IP = "localhost"
PORT = 8080

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