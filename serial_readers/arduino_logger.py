from SerialInstrument import SerialInstrument

ard_instr = SerialInstrument('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_75735303631351313102-if00', 9600, 'arduino_raw_data.csv', '/home/pi/Data/arduino/')

while True:
    try:
        reading = ard_instr.get_reading()
        ard_instr.write_output(reading)
    except Exception as e:
        print(str(e))
        ard_instr.close()
        break
