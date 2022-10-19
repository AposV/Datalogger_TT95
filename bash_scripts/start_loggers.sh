#!/bin/sh
python3 /home/pi/Datalogger_TT95/serial_readers/YP_logger.py &
python3 /home/pi/Datalogger_TT95/serial_readers/arduino_logger.py &
python3 /home/pi/Datalogger_TT95/serial_readers/libel_logger.py &
