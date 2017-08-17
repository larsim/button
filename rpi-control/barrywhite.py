import serial
import time
import os

cmdSetBaud = "\xA3\x3A\x03"
cmdSetChannel = "\xA7\x7A\x10"
cmdSetId = "\xA9\x9A\x00\x32"

DEVICE = '/dev/ttyUSB0'
BAUD = 19200

ser = serial.Serial(
    None,
    BAUD,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    dsrdtr = False
    )

ser.port = DEVICE

try: 
    ser.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()

ser.timeout = 2.0

ser.write(cmdSetBaud)
print("Serial: " + ser.read(1))
ser.write(cmdSetChannel)
print("Serial: " + ser.read(1))
ser.write(cmdSetId)
print("Serial: " + ser.read(1))
time.sleep(0.5)
  
def disco() :

  ser.timeout = 2.0

  # RGB On (length 72)
  print("RGB On")
  ser.write("R1,1130,553,77,65,69,72,73,")
  time.sleep(0.2)
  ser.write("66,76,65,70,72,73,65,77,")
  time.sleep(0.2)
  ser.write("65,69,72,74,206,70,210,")
  time.sleep(0.2)
  ser.write("77,207,73,206,70,210,76,")
  time.sleep(0.2)
  ser.write("207,73,206,70,210,77,")
  time.sleep(0.2)
  ser.write("207,73,206,70,210,76,")
  time.sleep(0.2)
  ser.write("65,70,71,73,65,76,65,")
  time.sleep(0.2)
  ser.write("70,72,73,65,77,65,69,")
  time.sleep(0.2)
  ser.write("72,74,206,70,210,77,")
  time.sleep(0.2)
  ser.write("206,74,206,70,210,77,")
  time.sleep(0.2)
  ser.write("4963,1126,275,70,65535,")
  time.sleep(0.5)
  print("Serial: " + ser.readline())

  # Play fireplace
  print("Playing fireplace...")
  os.system("omxplayer -b -o hdmi /home/pi/Fireplace_Barry.avi &")

  # Finish up after one minute
  time.sleep(60)

  # RGB Off (length 72)
  print("RGB Off")
  ser.write("R1,1127,557,73,65,77,65,69,")
  time.sleep(0.2)
  ser.write("72,73,66,76,65,70,72,73,65,")
  time.sleep(0.2)
  ser.write("77,65,69,211,76,207,73,207,")
  time.sleep(0.2)
  ser.write("69,211,76,207,73,207,70,210,")
  time.sleep(0.2)
  ser.write("76,207,73,66,76,207,73,207,")
  time.sleep(0.2)
  ser.write("69,72,74,65,76,65,70,72,73,")
  time.sleep(0.2)
  ser.write("65,76,206,73,66,76,65,70,210,")
  time.sleep(0.2)
  ser.write("77,206,73,206,70,211,76,207,")
  time.sleep(0.2)
  ser.write("73,4967,1124,275,76,65535,")
  time.sleep(0.5)
  print("Serial: " + ser.readline())
  time.sleep(2.0)

  # Cambridge DVD (?)
  print("Set Cambridge input source to DVD")
  ser.write("R1,127,96,232,208,232,103,117,103,")
  time.sleep(0.2)
  ser.write("117,103,117,103,117,103,117,103,")
  time.sleep(0.2)
  ser.write("117,103,117,103,117,208,117,65535,")
  time.sleep(0.5)
  ser.write("65535,")
  print("Serial: " + ser.readline())
  time.sleep(2.0)
  
ser.timeout = 60.0  

while True:
  if "DISCO!" in ser.readline(): 
    disco()
  print(time.strftime("%d/%m/%Y - %H:%M:%S"))
  
