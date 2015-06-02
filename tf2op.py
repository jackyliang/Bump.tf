#!/usr/bin/env python
import requests,json

tf2op_url = "http://www.tf2outpost.com/api/core"

# Parse tradeid.json
with open('tradeid.json') as data_file:    
    trade_id = json.load(data_file)

# TF2OP Cookie
uhash = trade_id['uhash'] 

cookies = { 
    'uhash':uhash
}

# Perform a bump on each trade
for tradeid in trade_id['tradeid']:
    payload = {
        'action':'trade.bump',
        'hash':uhash,
        'tradeid':tradeid
    }

    r = requests.post(
        tf2op_url,
        cookies=cookies,
        data=payload
    )

    print r.text
