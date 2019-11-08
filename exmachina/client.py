
import socket
import readline

from exmachina.protocol import send, recv

class SocketFileClient:

    def __init__(self, socket_file):
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.socket.connect(socket_file)

    def start(self):
        while True:
            try:
                i = input(">>> ")
                send(self.socket, i.encode("utf-8") + b"\n")
                print(recv(self.socket).decode("utf-8"), end="")
            except KeyboardInterrupt:
                break
        self.socket.close()
