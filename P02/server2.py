import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "localhost"  # it depends on the machine the server is running
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    server_socket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print(f"Waiting for connections at {IP}, {PORT} ")
        (client_socket, client_address) = server_socket.accept() #client adress es el ip y el puerto del cliente; el puerto del cliente se coge al azar; el ip seria el
        #de ese mismo ordenador, el 127.0.0.1

        # Another connection!e
        number_con += 1

        # Print the connection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, client_address))

        # Read the message from the client, if any
        msg = client_socket.recv(2048).decode("utf-8")
        print(f"Message from client: {msg}")

        # Send the message
        message = "Hello from the teacher's server\n"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        client_socket.send(send_bytes)
        client_socket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    server_socket.close()