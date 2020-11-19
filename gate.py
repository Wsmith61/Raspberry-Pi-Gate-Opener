import schedule
import time
#import RPi.GPIO as GPIO
from datetime import datetime
"""
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(19, True)
GPIO.output(13, True)
GPIO.output(6, True)
GPIO.output(12, True)
GPIO.output(16, True)
GPIO.output(20, True)
GPIO.output(21, True)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
"""
bc = 0
global gateclosed
gateclosed=False
global gateopen
gateopen=False
#bcflip = 0
def task():
    print("do task now")

def opengate():
    global gateclosed
    global gateopen
    #GPIO.output(26, False)
    print("opening gate")
    gateopen = True
    gateclosed = False

def closegate():
    global gateclosed
    global gateopen
    #GPIO.output(26, True)
    print("closing gate")
    gateopen = False
    gateclosed = True

def crestroninput():
    global input_state
    global bc
    #global bcflip
    #input_state = GPIO.input(4)
    if input_state == False:
        #bcflip = 1
        print('button pressed')
        opengate()
        bc += 1
    else:
        querrystate()
def querrystate():
    global bc
    time = int(str(datetime.now().time().hour)+str(datetime.now().time().minute))
    print(time)
    if time>2200 or time<700:
        closegate()
    elif bc>=2:
        closegate()
        print("bc")
        bc = 0
    else:
        opengate()

#schedule.every().day.at("07:00").do(opengate)
#schedule.every().day.at("22:00").do(closegate)

schedule.every().day.at("13:54").do(opengate)
schedule.every().day.at("13:56").do(closegate)



try:
    while True:
        schedule.run_pending()
        try:
            inkink = int(input())
            if inkink == 1:
                input_state = True
            elif inkink == 0:
                input_state = False
            crestroninput()
        except:
            pass
        if gateopen == True:
            print("gate is open")
        elif gateclosed == True:
            print("gate is closed")
        time.sleep(0.2)

while True:
    if gateopen == False:
        codein = input("get code")
        if codein in codes:
            opengate()
            print("Gate open")
            time.sleep(45)
            closegate()
            print("Gate closed")
        else:
            print("wrong code")

finally:
    #GPIO.cleanup()
    pass