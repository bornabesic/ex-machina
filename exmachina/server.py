
from threading import Thread
import socket

from .protocol import send, recv

class SocketFileServer(Thread):

    def __init__(self, socket_file, locals):
        super().__init__()
        self.locals = locals
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.socket.bind(socket_file)

    def eval_exec(self, line):
        try:
            val = eval(line, None, self.locals)
            return str(val) + "\n"
        except:
            try:
                exec(line, None, self.locals)
                return ""
            except Exception as e:
                return str(e) + "\n"

    def handle(self, connection):
        connected = True
        while connected:
            try:
                line = recv(connection)
                if not line:
                    continue
                output = self.eval_exec(line)
                send(connection, output.encode("utf-8"))
            except RuntimeError:
                connected = False
        connection.close()

    def run(self):
        while True:
            self.socket.listen(1)
            connection, address = self.socket.accept()
            Thread(target=self.handle, args=(connection,)).start()




