import socket

# Create a server socket

serverSocket = socket.socket()




# Associate the server socket with the IP/Host and Port

host = socket.gethostname()    # as both code is running on same pc

port = 5000

serverSocket.bind((host, port))

print("Socket is listening..")

print("Server socket bound with with ip {} port {}".format(host, port))

# Make the server listen for incoming connections

serverSocket.listen()

# Server incoming connections "one by one"

count = 0

while True:
    (client_Connection, client_Address) = serverSocket.accept()

    count = count + 1

    print("Accepted {} connections so far".format(count))

    # read from client connection

    while True:

        data = client_Connection.recv(1024).decode()
        end = data
        data_send = eval(data)                    #convert string into expression and evalute
        new_data_send = str(data_send)            #again convert result data into str

        if end == "end":
            print("Request done...")
            break



        client_Connection.send(str.encode(new_data_send))

        print("......")
