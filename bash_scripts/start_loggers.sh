#!/bin/sh
python3 /home/pi/Scripts/YP_logger.py &
python3 /home/pi/Scripts/arduino_logger.py &
python3 /home/pi/Scripts/libel_logger.py &
