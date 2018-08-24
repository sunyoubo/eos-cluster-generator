import socket
_IP = socket.gethostbyname(socket.gethostname())
MY_IP = "192.168.1.49"

IP = _IP if _IP == "127.0.0.1" else MY_IP
