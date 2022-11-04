import pandas as pd
from datetime import datetime
from os import walk

def swap_datetime_format(date, inplace=False):
    import_format = "%d-%m-%Y %H:%M:%S"
    export_format = "%Y-%m-%d %H:%M:%S"

    imp_date = datetime.strptime(date, import_format)
    exp_date = imp_date.strftime(export_format)
    if inplace:
        date = exp_date

    return exp_date


def swap_df_datetime_format(df):
    return df.Datetime.apply(lambda x: swap_datetime_format(x))


def swap_dt_frmt_recursively(old_folder, new_folder):
    for (dirpath, dirnames, filenames) in walk(old_folder):
        f.extend(filenames)
    print(f)


