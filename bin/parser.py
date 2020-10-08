#!/usr/bin/env python

# standard import
import json
import os
import sys

# third-party import
import numpy as np


if '__main__' == __name__:
    data = json.load(open(f'/home/mlb/res/stock/twse/json/{sys.argv[1]}.json'))
    diff_set = {code: float(stock['close']) - float(stock['open']) for code, stock in data.items() if code != 'id' and stock['close'] != 'NULL' and stock['open'] != 'NULL'}
    diff_set_sorted = sorted(diff_set.items(), key=lambda x:abs(x[1]), reverse=True)
    decision_set = []

    for (code, diff) in diff_set_sorted[:10]:
        curr_stock = data[code]
        curr_decision = {
	    "code": code,
	    "life": 3,
	    "type": "buy" if diff > 0 else "short",
	    "weigth": 1,
	    "open_price": float(curr_stock['close']),
	    "close_high_price": float(curr_stock['close']) + abs(diff),
	    "close_low_price": float(curr_stock['close']) - abs(diff)       
        }
        decision_set.append(curr_decision)
    if not os.path.exists('../commit/'):
        os.makedirs('../commit/')
    json.dump(decision_set, open(f'../commit/{sys.argv[1]}_{sys.argv[1]}.json', 'w'), indent=4)
