"""This file contains a dictionary containing various naming configurations
that are used in the monitoring system to avoid hardcoding them in scripts
and make updating easier"""

naming_config = {
    'yp_inst_ids': {'ext1': '1903210671',
                    'ext2': '1903210681',
                    'rta': '1904112001'},

    'raw_data_folder_location': '/home/pi/Data',

    'raw_data_instrument_folders': {'yp': 'YP',
                                    'arduino': 'arduino',
                                    'libelium': 'libelium'},

    'raw_data_master_filenames': {'arduino': 'arduino_raw_data.csv',
                                    'yp': 'YP_raw_data.csv',
                                    'libelium': 'libelium_raw_data.csv'},

    'db_table_columns': {'ext1': ('datetime', 'air_temp', 'apperture'),
                         'ext2': ('datetime', 'air_temp', 'apperture'),
                         'rta': ('datetime', 't1', 't2', 't3',
                               't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11'),
                         'arduino': ('datetime', 't1', 't2', 't3',
                               't4', 't5', 't6', 'luminosity'),
                         'libelium': ('datetime', 'epoch_time', 'battery_level',
                                      'dendrometer', 't1', 'r_humid', 'atm_p',
                                      't2', 'voltage')},

    'raw_csv_columns': {'yp': ['Datetime', 'Datapoint_no', 'Order', 'Year', 'Month', 'Day', 'Hour',
                               'Minute', 'Second', 'Inst_id', 't1', 't2', 't3',
                               't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12'],
                        'arduino': ['Datetime', 't1', 't2', 't3',
                                    't4', 't5', 't6', 'luminosity'],
                        'libelium': ['Datetime', 'epoch_time', 'battery_level',
                                     'dendrometer', 't1', 'rhumid', 'atm_p', 't2', 'voltage']},

}
