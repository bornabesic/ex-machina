# ⚙️ ex-machina
Access the state of a running program via socket-based REPL

## Installation
```sh
pip install git+https://github.com/bornabesic/ex-machina
```

## Usage

### Server
```python
from exmachina import SocketFileServer

exposed_variables = locals()
server = SocketFileServer("/tmp/exmachina.sock", exposed_variables)
server.start() # Runs the server in a separate thread
```

### Client
```python
from exmachina import SocketFileClient

client = SocketFileClient("/tmp/exmachina.sock")
client.start() # REPL; loops infinitely (press Ctrl+C to exit)
```
