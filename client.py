'''
    Course: CS3622
    Student: Elliot Larez
    ID: 001019387
'''

import socket

# creates a socket for the client
# AF_INET for IPv4 internet socket
# SOCK_STREAM for connection based
# IPPROTO_TCP for TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# sets the host and port of the client
client_host_name = socket.gethostname()
client_host = socket.gethostbyname(client_host_name)
client_port = 5123

# specifies the host and port where the client socket will be bound
client_socket.bind((client_host, client_port))

# prints the host and port of the client
print('Client created')
print("\thost name: " + client_host_name)
print("\thost: " + client_host)
print("\tport: " + str(client_port))

# sets the host and port of the server
server_host = input('Introduce server Host: ')
server_port = int(input('Introduce server Port: '))

# connects to the server
client_socket.connect((server_host, server_port))

print('\tConnection established with {}:{}'.format(server_host, server_port))

is_client_running = True
buffer_size = 1024
encoding = 'utf-8'

while is_client_running:

    # sends a message to the server
    input_message = input('\t\tIntroduce a message: ')
    client_socket.send(input_message.encode())

    print('\t\tMessage Sent: ', input_message)

    # receives a response from the server
    received_data = client_socket.recv(1024)
    received_message = received_data.decode()

    print('\t\tMessage Receive: ', received_message)

    if received_message == 'dne':
        print('\tConnection ended with {}:{}'.format(server_host, server_port))

        # close the server's socket
        client_socket.close()

        print('Client deleted')
        is_client_running = False
        break
