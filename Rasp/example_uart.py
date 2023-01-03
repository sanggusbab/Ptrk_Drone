import serial
while True:
    ser = serial.Serial ("/dev/serial0")    #Open named port 
    ser.baudrate = 57600                     #Set baud rate to 57600
    data = ser.read(10)                     #Read ten characters from serial port to data
    ser.write(data)                         #Send back the received data
    print(data)
    ser.close()