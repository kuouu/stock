import sys
import json
import pandas as pd
import numpy as np

date = sys.argv[1]
read_day = eval(sys.argv[2])

stock = np.empty([0,6])

for single_date in pd.date_range(end=date, periods=read_day, freq='B', closed='left'):
#     print(single_date)
    try: 
        data =  json.load(open('/home/mlb/res/stock/twse/json/'+single_date.strftime("%Y-%m-%d")+'.json'))
        day_data = []
        for key in data['2330']:
            day_data.append(eval(data['2330'][key]))
        day_data = np.array(day_data)
        stock = np.vstack((stock, day_data))
    except:
        continue

np.save('../output/data', stock[:,1:])
