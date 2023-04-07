'''
    Course: CS3622
    Student: Elliot Larez
    ID: 001019387
'''
import socket


# returns a given string in reverse order
def reverse_string(s:str):
    reverse_s = ''
    for i in s:
        reverse_s = i + reverse_s
    return reverse_s


# creates a socket for the server
# AF_INET for IPv4 internet socket
# SOCK_STREAM for connection based
# IPPROTO_TCP for TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# sets the host and port of the server
server_host_name = socket.gethostname()
server_host = socket.gethostbyname(server_host_name)
server_port = 5100

# specifies the host and port where the server socket will be bound
server_socket.bind((server_host, server_port))

# prints the host and port of the server
print('Server created')
print("\thost name: " + server_host_name)
print("\thost: " + server_host)
print("\tport: " + str(server_port))

# Specifies maximum number of connections that the server socket will be bound
maximum_connections = 1
server_socket.listen(maximum_connections)

# waits for a client to connect
print('Waiting for client')
client_socket, client_addr = server_socket.accept()
client_host = client_addr[0]
client_port = client_addr[1]

print('\tConnection established with {}:{}'.format(client_host, client_port))

is_server_running = True
buffer_size = 1024
encoding = 'utf-8'

while is_server_running:

    # receives a message from the client
    received_data = client_socket.recv(buffer_size)
    while not received_data:
        received_data = client_socket.recv(buffer_size)
    received_message = received_data.decode(encoding)

    print('\t\tMessage Received: ', received_message)

    # send a response to the client
    response_message = reverse_string(received_message)
    client_socket.send(response_message.encode(encoding))
    print('\t\tMessage Sent: ', response_message)

    if received_message == 'end':
        # close the client's socket
        client_socket.close()
        print('\tConnection ended with {}:{}'.format(client_host, client_port))

        # close the server's socket
        server_socket.close()

        print('Server deleted')
        is_server_running = False
        break
