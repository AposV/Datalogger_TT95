import json
import sys

import pandas as pd

from datetime import datetime, timedelta
from TT95_Helper.db_helpers import MySQLConnector
from TT95_Helper import configurations
from TT95_Helper import datetime_handlers as dth

name_config = configurations.naming_config
data_folder = name_config['raw_data_folder_location']

# Call the script as: python3 upload_data_in_date_range.py 'start_date' 'end_date'
# IMPORTANT: Use underscore instead of dashes in the date format
# Example: python3 upload_data_in_date_range.py '2023_03_29' '2023_05_26'
start_date = sys.argv[1]
stop_date = sys.argv[2]

print(start_date)
print(stop_date)

yp_filepath = f"{data_folder}/{name_config['raw_data_instrument_folders']['yp']}/" \
              f"{name_config['raw_data_master_filenames']['yp']}"

libel_filepath = f"{data_folder}/{name_config['raw_data_instrument_folders']['libelium']}/" \
              f"{name_config['raw_data_master_filenames']['libelium']}"

arduino_filepath = f"{data_folder}/{name_config['raw_data_instrument_folders']['arduino']}/" \
              f"{name_config['raw_data_master_filenames']['arduino']}"


# Process Yieldpoint Sensors and clean data
yp_data = pd.read_csv(yp_filepath, names=name_config['raw_csv_columns']['yp'])


# Separate data for each extensometer and the rock temp array
ext1_df = yp_data[yp_data['Inst_id'] == name_config['yp_inst_ids']['ext1']]
ext2_df = yp_data[yp_data['Inst_id'] == name_config['yp_inst_ids']['ext2']]
rta_df = yp_data[yp_data['Inst_id'] == name_config['yp_inst_ids']['rta']]


ext1_data = ext1_df.loc[:,['Datetime', 't1', 't2']]
ext2_data = ext2_df.loc[:,['Datetime', 't1', 't2']]
rta_data = rta_df.loc[:,['Datetime', 't1', 't2', 't3', 't4', 't5',
                  't6', 't7', 't8', 't9', 't10', 't11']]


# Process Libelium Sensors and clean data
libelium_data = pd.read_csv(libel_filepath, names=name_config['raw_csv_columns']['libelium'])
libelium_data = libelium_data.dropna()

# Process arduino Sensors and clean data
arduino_data = pd.read_csv(arduino_filepath, names=name_config['raw_csv_columns']['arduino'])
arduino_data = arduino_data.dropna()

ext1_data = ext1_data[(ext1_data['Datetime'] >= start_date) & (ext1_data['Datetime'] <= stop_date)]
ext2_data = ext2_data[(ext2_data['Datetime'] >= start_date) & (ext2_data['Datetime'] <= stop_date)]
rta_data = rta_data[(rta_data['Datetime'] >= start_date) & (rta_data['Datetime'] <= stop_date)]
arduino_data = arduino_data[(arduino_data['Datetime'] >= start_date) & (arduino_data['Datetime'] <= stop_date)]

print('----------------')
print(yp_data)
print('----------------')
print(libelium_data)
print('----------------')
print(arduino_data)


# Read database configuration file and establish connection to the database
with open('db_config.json', 'r') as read_file:
    db_config = json.load(read_file)

conn = MySQLConnector(db_config)

'''
# Upload data from each sensor to the database
conn.upload_table(ext1_data, name_config['db_table_columns']['ext1'], 'extensometer_1', False)
conn.upload_table(ext2_data, name_config['db_table_columns']['ext2'], 'extensometer_2', False)
conn.upload_table(rta_data, name_config['db_table_columns']['rta'], 'rock_temp_array', False)
conn.upload_table(arduino_data, name_config['db_table_columns']['arduino'], 'arduino_tt95', False)
conn.upload_table(libelium_data, name_config['db_table_columns']['libelium'], 'libelium', False)

# Commit changes to the database and close connection
conn.commit()
conn.close()'''


