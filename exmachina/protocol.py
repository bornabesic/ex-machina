
import sys
import socket

INTEGER_BYTES = 8

def send(socket, bytes):
    length = len(bytes)
    length_header = length.to_bytes(length=INTEGER_BYTES, byteorder=sys.byteorder)
    socket.sendall(length_header + bytes)

def _ensure_recv(socket, n_bytes):
    data = bytes()
    while len(data) < n_bytes:
        r = socket.recv(n_bytes - len(data))
        if not r:
            raise RuntimeError
        data += r
    return data

def recv(socket):
    length_header = _ensure_recv(socket, INTEGER_BYTES)
    length = int.from_bytes(length_header, byteorder=sys.byteorder)
    if length > 0:
        return _ensure_recv(socket, length)
    return bytes()