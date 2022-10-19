#!/bin/sh
python3 /home/pi/Datalogger_TT95/bash_scripts/YP_logger.py &
python3 /home/pi/Datalogger_TT95/bash_scripts/arduino_logger.py &
python3 /home/pi/Datalogger_TT95/bash_scripts/libel_logger.py &
