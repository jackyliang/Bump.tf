#!/usr/bin/env python
import requests,json

# Constants
tf2op_url = "http://www.tf2outpost.com/api/core"
tf2op_db = "tradeid.json"

# Parse tradeid.json
with open(tf2op_db) as data_file:    
    trades = json.load(data_file)

# Perform a bump on each trade
for trade in trades:

    uhash = trade['uhash'] 
    
    cookies = { 
        'uhash':uhash
    }

    for tradeid in trade['tradeid']: 

        payload = {
            'action':'trade.bump',
            'hash':trade['uhash'],
            'tradeid':tradeid
        }

        r = requests.post(
            tf2op_url,
            cookies=cookies,
            data=payload
        )

        print r.text
