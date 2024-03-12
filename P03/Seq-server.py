import socket
import termcolor
from Seq1 import Seq1
import os

IP = "localhost"
PORT = 8080

SEQUENCES = ["GGCGT", "ACTTG", "ATCGC", "CCTAC", "GTCAT"]
BASES_VALUE = {"A": 2, "C": -1, "G": 3, "T": 5}

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
        elif command == "INFO" and len(slices) == 2:
            bases = slices[1]
            try:
                for character in bases:
                    if character != 'A' and character != 'C' and character != 'G' and character != 'T':
                        response = "ERROR"
                    else:
                        sequence = Seq1(bases)
                        response = sequence.info()
            except ZeroDivisionError:
                response = "ERROR"
        elif command == "COMP" and len(slices) == 2:
            bases = slices[1]
            for character in bases:
                if character != 'A' and character != 'C' and character != 'G' and character != 'T':
                    response = "ERROR"
                else:
                    sequence = Seq1(bases)
                    response = sequence.complement()
        elif command == "REV" and len(slices) == 2:
            bases = slices[1]
            for character in bases:
                if character != 'A' and character != 'C' and character != 'G' and character != 'T':
                    response = "ERROR"
                else:
                    sequence = Seq1(bases)
                    response = sequence.reverse()
        elif command == "GENE" and len(slices) == 2:
            gene = slices[1]
            if gene != "U5" and gene != "ADA" and gene != "FRAT1" and gene != "FXN" and gene != "RNU6_269P":
                response = "Error"
            else:
                file_name = os.path.join("..", "Genes", gene + ".txt")
                s = Seq1()
                s.read_fasta(file_name)
                response = s.bases #response = str(s)
        elif command == "MULT" and len(slices) == 2:
            bases = slices[1]
            s = Seq1(bases)
            if s.is_valid():
                response = str(s.mult())
                #V1
            #if Seq1.are_bases_ok(bases):
                #total = 1
                #for base in bases:
                    #total *= BASES_VALUE[base]
                    # response = f"{total}"
                    #V2
                    #if base == "A":
                        #total *= 2 #total = total * 2
                    #elif base == "C":
                        #total *= -1
                    #elif base == "G":
                        #total *= 3
                    #else:
                        #total *= 5
                #response = f"{total}" #response = str(total) + "\n"
            else:
                response = "We could not multiply the bases since the sequence is not correct"
        elif command == "DIV" and len(slices) == 2:
            bases = slices[1]
            if Seq1.are_bases_ok(bases):
                total = 1
                try:
                    for base in bases:
                        d = BASES_VALUE[base]
                        result  = d // total
                        response = f"{result}"
                except ZeroDivisionError:
                    print("Error")
            else:
                response = "We could not divide the bases since the sequence is not correct"


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