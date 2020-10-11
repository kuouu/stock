. ../../env01/bin/activate

python3 load.py $1 100

python3 predict.py

python3 make_decision.py ../commit/$1_$1.json