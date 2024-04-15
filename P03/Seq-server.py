import socket
import termcolor
from Seq1 import Seq1
import os
IP = "localhost"
PORT = 8081

SEQUENCES = ["ACTGA", "CCTTG", "AAGAG", "GGGGG", "ACACC"]


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    print("SEQ Server configured")
    while True:
        print(f"Waiting for clients...")
        (client_socket, client_address) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode("utf-8")
        slices = request.split(" ") #esto te devuelve el string separado en una lista por ejemplo get1 = ["get" "1"]
        command = slices[0]
        termcolor.cprint(f"{command} command!", 'green')

        response = ""
        if command == "PING":
            response = "OK!\n"
        elif command == "GET" and len(slices) == 2:
            try:
                n = int(slices[1])
                if 0 <= n < len(SEQUENCES):
                    response = SEQUENCES[n] + "\n"
                else:
                    response = f"Sequence with {n} index not found"
            except ValueError:
                response = ""
        elif command == "INFO" and len(slices) == 2:
            bases = slices[1]
            for character in bases:
                try:
                    if character != 'A' and character != 'C' and character != 'G' and character != 'T':
                        response = "ERROR" + "\n"
                    else:
                        sequence = Seq1(bases)
                        response = sequence.info() + "\n"
                except ZeroDivisionError:
                    response = "ERROR" + "\n"
        elif command == "COMP" and len(slices) == 2:
            bases = slices[1]
            for character in bases:
                if character != 'A' and character != 'C' and character != 'G' and character != 'T':
                    response = "ERROR" + "\n"
                else:
                    sequence = Seq1(bases)
                    response = sequence.complement() + "\n"
        elif command == "REV" and len(slices) == 2:
            bases = slices[1]
            for character in bases:
                if character != 'A' and character != 'C' and character != 'G' and character != 'T':
                    response = "ERROR" + "\n"
                else:
                    sequence = Seq1(bases)
                    response = sequence.reverse() + "\n"
        elif command == "GENE" and len(slices) == 2:
            gene = slices[1]
            if gene != 'U5' and gene != 'FRAT1' and gene != 'FXN' and gene != 'RNU6_269P':
                    response = "ERROR" + "\n"
            else:
                file_name = os.path.join("..", "Genes", gene + ".txt")
                s = Seq1()
                s.read_fasta(file_name)
                response = s.bases + "\n"  #response = str(s)
        else:
            response = "ERROR: Command not found"

        print(response)

        response_bytes = str.encode(response)
        client_socket.send(response_bytes)

        client_socket.close()

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")
except KeyboardInterrupt:
    print("Server stopped by the admin")
    server_socket.close()