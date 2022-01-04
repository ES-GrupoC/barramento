import socket
import json
import sys

if len(sys.argv) != 3:
    print('numero de argumentos invalido:{} \n codigo a executar: \n python client.py speed dir \n'.format(len(sys.argv)))
    exit(1)
values = {'speed': int(sys.argv[1]), 'dir': int(sys.argv[2])}
serialized_values = json.dumps(values)

sock = socket.socket()
host = socket.gethostname()
port = 1218

try:
    sock.connect((host, port))
    sock.sendall(bytes(serialized_values, encoding='utf-8'))
finally:
    sock.close()

print('sent:  {}'.format(serialized_values))

