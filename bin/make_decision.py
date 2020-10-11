import json
import sys

filename = sys.argv[1]
predict = open('../output/predict', 'r')

open_price = eval(predict.read())
close_high_price = open_price + open_price * 0.1
close_low_price = open_price - open_price * 0.2
predict.close()

operation = {
    "code":2330,
    "type":"buy",
    "open_price":open_price,
    "weight":1,
    "close_high_price": close_high_price,
    "close_low_price": close_low_price,
    "life": 5,
}


output = []

output.append(operation)
output = json.dumps(output)

with open(filename, 'w') as outfile:
    outfile.write(output)