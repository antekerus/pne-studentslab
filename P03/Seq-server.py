import socket
import termcolor
from Seq1 import Seq1
import os

IP = "localhost"
PORT = 8080

SEQUENCES = ["GGCGT", "ACTTG", "ATCGC", "CCTAC", "GTCAT"]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    print("SEQ Server configured!")
    while True:
        print("Waiting for clients...")
        (client_socket, client_address) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode("utf-8")
        slices = request.split(" ")
        command = slices[0]
        termcolor.cprint(f"{command} command!", "green")

        response = ""
        if command == "PING":
            response = "OK!"
        elif command == "GET" and len(slices) == 2:
            try:
                n = int(slices[1])
                if 0 <= n < len(SEQUENCES):
                    response = SEQUENCES[n]
                else:
                    response = f"Sequence with {n} index not found"
            except ValueError:
                response = "..."
        elif command == "INFO":
            bases = slices[1]
            s = Seq1(bases)
            response = s.info()
        elif command == "COMP":
            bases = slices[1]
            s = Seq1(bases)
            response = s.complement()
        elif command == "REV":
            bases = slices[1]
            s = Seq1(bases)
            response = s.reverse()
        elif command == "GENE":
            gene = slices[1]
            file_name = os.path.join("..", "Genes", gene + ".txt")
            s = Seq1()
            s.read_fasta(file_name)
            response = s.bases #response = str(s)
        elif command == "MULT":
            bases = slices[1]
        else:
            response = "ERROR: Command not found"

        response += "\n"
        print(response)
        response_bytes = str.encode(response)
        client_socket.send(response_bytes)

        client_socket.close()

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")
except KeyboardInterrupt:
    print("Server stopped by the admin")
    server_socket.close()
