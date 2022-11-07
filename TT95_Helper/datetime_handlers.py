import os
import pandas as pd

from TT95_Helper import configurations
from datetime import datetime, timedelta

names_config = configurations.naming_config


def swap_datetime_format(date, inplace=False):
    """Swaps datetime format from "%d-%m-%Y %H:%M:%S" to "%Y-%m-%d %H:%M:%S".

    date: the date that needs to be reformatted

    returns: reformatted date string"""
    import_format = "%d-%m-%Y %H:%M:%S"
    export_format = "%Y-%m-%d %H:%M:%S"

    imp_date = datetime.strptime(date, import_format)
    exp_date = imp_date.strftime(export_format)
    if inplace:
        date = exp_date

    return exp_date


def swap_df_datetime_format(df):
    """Reformats the datetimes of the dataframe df, containing a 'Datetime' column"""
    df.Datetime = df.Datetime.apply(lambda x: swap_datetime_format(x, inplace=True))
    return df


def swap_dt_frmt_recursively(old_folder, new_folder):
    """Reformats the dates in the csv files made by the TT95 logger. Works
    recursively reformatting every file in every subfolder in oldfolder and saves
    the reformatted files in new folder maintaining the subfolder structure of oldfolder"""
    dir = os.listdir(old_folder)
    names = None
    for d in dir:
        of = old_folder + '/' + d
        nf = new_folder + '/' + d
        if os.path.isfile(of) & ('csv' in of):
            print('Reading: ' + of)
            if 'arduino' in of:
                names = names_config['raw_csv_columns']['arduino']
            elif 'YP' in of:
                names = names_config['raw_csv_columns']['yp']
            elif 'libelium' in of:
                names = names_config['raw_csv_columns']['libelium']

            old_df = pd.read_csv(of, names=names)
            new_df = swap_df_datetime_format(old_df)
            new_df.to_csv(nf, index=False, header=False)
            print('Writing: ' + nf)
        else:
            swap_dt_frmt_recursively(of, nf)


def get_prev_day_data_file(sensor):
    prev_date = (datetime.today() - timedelta(days=1)).strftime('%Y_%m_%d')
    filepath = names_config['raw_data_folder_location'] + '/' + \
                  names_config['raw_data_instrument_folders'][sensor] + '/backup/' + \
                  prev_date + '_' + names_config['raw_data_master_filenames'][sensor]

    return filepath