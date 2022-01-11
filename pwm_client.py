import socket
import json
import sys

if len(sys.argv) != 3:
    print('numero de argumentos invalido:{} \n codigo a executar: \n python pwm_client.py speed dir \n'.format(len(sys.argv)))
    exit(1)

speed = int(sys.argv[1])
direction = int(sys.argv[2])

speed = speed*21.25
if direction == 1:
    dir_duty = 0
elif direction == 2:
    dir_duty = 255
else:
    dir_duty = 128

values = {'speed': int(speed), 'dir': int(dir_duty)}
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
