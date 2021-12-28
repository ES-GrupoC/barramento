import sys 
import RPi.GPIO as GPIO

#argv[1] = speed »» 5 -> 12 Km/h
#argv[2] = dir »» 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
my_pwm_speed=GPIO.PWM(33,100)
my_pwm_speed.start(0)
my_pwm_dir=GPIO.PWM(32,100)
my_pwm_dir.start(0)


def update_speed(speed):
    duty = int(speed*14.286 -71.429)
    print('dutycicle for speed: ', duty)
    my_pwm_speed.ChangeDutyCycle(duty)
    return 0

update_speed(sys.argv[1])

def update_dir(direction):
    #duty = ....
    #print('dutycicle for dir: ', duty)
    #my_pwm_dir.ChangeDutyCycle(duty)
    #return 0
