import serial
import time

###################################################
##   USB Comunication ARDUI-Rasp  /Raspberry Code ##
###################################################


ser=serial.Serial('/dev/ttyACM0',9600)
while 1:
        print(ser.readline())
        ser.write('091')
        time.sleep(1)
        ser.write('090')
        time.sleep(1)