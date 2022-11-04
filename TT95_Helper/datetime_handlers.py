import pandas as pd
from datetime import datetime
import os
from TT95_Helper import configurations

names_config = configurations.naming_config


def swap_datetime_format(date, inplace=False):
    import_format = "%d-%m-%Y %H:%M:%S"
    export_format = "%Y-%m-%d %H:%M:%S"

    imp_date = datetime.strptime(date, import_format)
    exp_date = imp_date.strftime(export_format)
    if inplace:
        date = exp_date

    return exp_date


def swap_df_datetime_format(df):
    df.Datetime.apply(lambda x: swap_datetime_format(x, inplace=True))
    return df


def swap_dt_frmt_recursively(old_folder, new_folder):
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
            new_df.to_csv(nf)
            print('Writing: ' + nf)
        else:
            swap_dt_frmt_recursively(of, nf)