import http.client
import json

GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

SERVER = 'rest.ensembl.org'
RESOURCE = f'/sequence/id/{GENES["MIR633"]}'
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
    print("Gene: MIR633")
    print(f"Description: {data['desc']}")
    print(f"Bases: {data['seq']}")

