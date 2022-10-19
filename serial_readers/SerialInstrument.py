import pandas as pd
import serial
import time
import csv
from datetime import datetime

'''
Abstract Class for a serial reader

Subclass SerialInstrument for each connected device and implement
new methods as desired to extend functionality
'''
class SerialInstrument():

    def __init__(self, serial_port, baud_rate, output_file, out_file_path):
        self.instrument = serial.Serial(serial_port, baud_rate)
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.output_file = output_file
        self.out_file_path = out_file_path


    def get_reading(self, encoding='utf-8'):
        reading = self.instrument.readline()
        if encoding: reading = reading.decode(encoding)
        return reading


    def write_output(self, reading):
        now = datetime.now()
        date_file = now.strftime("%m_%d_%Y")
        with open(self.out_file_path + self.output_file, "a") as f:
            f.write(now.strftime("%d-%m-%Y %H:%M:%S")+ ',' +reading)
        with open(self.out_file_path +
                  'backup/'+
                  date_file+'_'+self.output_file, "a") as f:
            f.write(now.strftime("%d-%m-%Y %H:%M:%S")+ ',' +reading)



    def close(self):
        self.instrument.close()
