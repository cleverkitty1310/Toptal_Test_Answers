import pandas as pd
import numpy as np
import os 
from dateutil import parser


path = './csv_files'
files = os.listdir(path)
res = []
for file in files:
    file = os.path.join(path, file)
    df = pd.read_csv(file)
    df['year'] = pd.DatetimeIndex(df['date']).year
    df = df[['date', 'vol', 'year', 'close']]
    groups = df.groupby('year')
    years = sorted(list(df['year'].unique()))
    vol_dates = []
    vols = []
    close_dates = []
    closes = []
    for year in years:
        group = groups.get_group(year)
        idx = group['vol'].argmax()
        vol = group.iloc[idx].vol
        date = group.iloc[idx].date
        date = parser.parse(date)
        vol_dates.append(date)
        vols.append(vol)

        close_data = np.array(group['close'])
        idxs = np.where(close_data == close_data.max())[0]
        group = np.array(group)
        close = group[idxs, 3]
        date = group[idxs, 0]
        for i in range(date.__len__()):
            date[i] = parser.parse(date[i])
        close_dates.append(date)
        closes.append(close)

    vol_dates = pd.Series(vol_dates, name = 'date')
    vols = pd.Series(vols, name = 'vol')
    fi_res = pd.concat([vol_dates, vols], axis = 1)
    closes = list(np.concatenate(closes).flat)
    close_dates = list(np.concatenate(close_dates).flat)
    close_dates = pd.Series(close_dates, name = 'date')
    closes = pd.Series(closes, name = 'close')
    sec_res = pd.concat([close_dates, closes], axis = 1)
    res.append([fi_res, sec_res])

print(res)