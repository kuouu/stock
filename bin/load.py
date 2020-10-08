import sys
import json

data = json.load(open(f'/home/mlb/res/stock/twse/json/{sys.argv[1]}.json'))
for key in data.keys():
    print('key:%s value: %s' % (key, data.get(key)))
