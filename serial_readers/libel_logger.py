from TT95Logger import SerialInstrument

libel_instr = SerialInstrument('/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AH06GGYC-if00-port0', 115200, 'libelium_raw_data.csv', '/home/pi/Data/libelium/')

while True:
    try:
        reading = libel_instr.get_reading()
        libel_instr.write_output(reading)
    except Exception as e:
        print(str(e))
        libel_instr.close()
        break
