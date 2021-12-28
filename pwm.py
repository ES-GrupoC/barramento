import sys 
import RPi.GPIO as GPIO

'''
argv[1] = speed »» 5 -> 12 Km/h
argv[2] = dir »» 1-esquerda 0-nao faz nada 2->direita

'''

#config.py############################################
GPIO.setwarnings(False)                             ##         
GPIO.setmode(GPIO.BOARD)                            ##       
GPIO.setup(33,GPIO.OUT)                             ##           
GPIO.setup(32,GPIO.OUT)                             ##           
my_pwm_speed=GPIO.PWM(33,100)                       ##      
my_pwm_speed.start(0)                               ##     
my_pwm_dir=GPIO.PWM(32,100)                         ##       
my_pwm_dir.start(0)                                 ##        
######################################################


def update_speed(speed):
    duty = int(int(speed)*8.5714 - 17.857)
    #print('dutycicle for speed: ', duty)
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
    #print('dutycicle for dir: ', duty)
    my_pwm_dir.ChangeDutyCycle(duty)
    return 0


if int(sys.argv[2]) == 0:
    update_speed(sys.argv[1])

if int(sys.argv[2]) > 0:
    update_dir(sys.argv[2])

i=0
while True:
    i+=1