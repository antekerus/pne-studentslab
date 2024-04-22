import http.client
import json

SERVER = 'rest.ensembl.org'
RESOURCE = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + RESOURCE + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", RESOURCE + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
response = conn.getresponse()

# -- Print the status line
print(f"Response received!: {response.status} {response.reason}\n")

if response.status == 200:
    # -- Read the response's body
    data_str = response.read().decode("utf-8")

    # -- Create a variable with the data,
    # -- form the JSON received
    data = json.loads(data_str)
    ping = data["ping"]
    if ping == 1:
        print("PING OK! The database is running!")
    else:
        print("ERROR")

