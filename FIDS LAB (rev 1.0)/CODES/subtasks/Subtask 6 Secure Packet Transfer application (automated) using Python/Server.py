import socket
import tkinter as tk
from tkinter import messagebox
import threading
import sys

# Create a socket for communication
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(1)
Obtained_Messages = []

# Create a tkinter window for server logs
root = tk.Tk()
root.title("Incoming Message Transfers Log")
text_area = tk.Text(root)
text_area.pack()

def update_text_area(text):
    text_area.insert(tk.END, text)
    text_area.see(tk.END)

# Define a function to handle incoming messages
def handle_message(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        response = messagebox.askyesno("Incoming Message Detected:", f"Accept Message \"{data}\"?")
        if response:
            update_text_area(f"Granted Transfer: \"{data}\"\n")
            Obtained_Messages.append(data)
        else:
            update_text_area(f"Denied Transfer: \"{data}\"\n")
        print("Messages Granted: ", end="")
        print(Obtained_Messages)

# Writing the Messages into a Textfile to ensure Packet Source Code – Client
with open("Messages.txt", "w") as f:
    for Msg in Obtained_Messages:
        f.write(f"{Msg}\n")

# Accept incoming connections
print("Waiting for incoming connection...")

def accept_connections():
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            # Create a thread to handle the client
            client_thread = threading.Thread(target=handle_message, args=(client_socket,))
            client_thread.start()
        except KeyboardInterrupt:
            print("Server interrupted. Closing server socket.")
            server_socket.close()
            sys.exit()

# Create a thread to accept connections
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()

# Start the tkinter main loop
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Server interrupted. Exiting.")
    sys.exit()
