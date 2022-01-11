import socket
import json
import threading
import serial
import time


serialcomm = serial.Serial('com4', 9600)
serialcomm.timeout = 1


def serial_send_buffer(buffer):
    print('\n buffer : ', buffer)
    serialcomm.write(buffer.encode())
    time.sleep(0.5)
    return 0


def update_signal(pwms_signals):
    buffer = str(pwms_signals['speed']) + ',' + str(pwms_signals['dir'])
    serial_send_buffer(buffer)
    return 0


def my_task(info):
    info = json.loads(info)
    update_signal(info)


oneConnectionOnly = False
port = 1218
sock = socket.socket()
host = socket.gethostname()
sock.bind((host, port))
sock.listen(10)


while True:
    conn, address = sock.accept()
    print(f'Accepted connection from {address}')
    serialized_values = conn.recv(1024)
    values = serialized_values.decode('utf-8')
    conn.close()
    t = threading.Thread(target=my_task, args=(values,))
    t.start()
    if oneConnectionOnly:
        break
sock.shutdown(1)
sock.close()
