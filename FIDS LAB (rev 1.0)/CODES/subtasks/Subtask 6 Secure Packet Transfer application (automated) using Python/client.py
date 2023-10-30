import socket
import threading

# Create a socket for communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.72.250", 12345))  # Replace with the server's IP address

# Function to send messages to the server
def send_message():
    while True:
        message = input("Enter the message to be Sent to other Computer: ")
        client_socket.send(message.encode())

# Create a thread to send messages
send_thread = threading.Thread(target=send_message)
send_thread.start()
