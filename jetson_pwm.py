import socket
import json
import threading
import RPi.GPIO as GPIO


#config.py############################################
GPIO.setwarnings(False)                             ##
GPIO.setmode(GPIO.BOARD)                            ##
GPIO.setup(33, GPIO.OUT)                            ##
GPIO.setup(32, GPIO.OUT)                            ##
my_pwm_speed = GPIO.PWM(33, 100)                    ##
my_pwm_speed.start(0)                               ##
my_pwm_dir = GPIO.PWM(32, 100)                      ##
my_pwm_dir.start(0)                                 ##
######################################################


def update_speed(speed):
    duty = int(int(speed)*8.5714 - 17.857)
    print('dutycicle for speed: ', duty)
    my_pwm_speed.ChangeDutyCycle(duty)
    return 0


def update_dir(direction):
    '''
    full foward -> direita
    full reverse -> esquerda
    '''
    if int(direction) == 1:
        duty = 25
    else:
        duty = 85
    print('dutycicle for dir: ', duty)
    my_pwm_dir.ChangeDutyCycle(duty)
    return 0


def my_task(info):
    info = json.loads(info)
    if int(info['dir']) == 0:
        update_speed(int(info['speed']))
    elif int(info['dir']) > 0:
        update_dir(int(info['dir']))


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
