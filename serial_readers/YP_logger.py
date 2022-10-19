from TT95Logger import SerialInstrument

yp_instr = SerialInstrument('/dev/serial/by-id/usb-FTDI_TTL232R_FTC23PQY-if00-port0', 9600, 'YP_raw_data.csv', '/home/pi/Data/YP/')

while True:
    try:
        reading = yp_instr.get_reading()
        if 'sync' not in reading:
            print(reading)
            yp_instr.write_output(reading)
    except Exception as e:
        print(str(e))
        yp_instr.close()
        break
