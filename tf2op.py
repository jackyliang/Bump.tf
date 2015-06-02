#!/usr/bin/env python
import requests,json,os.path,sys
from datetime import datetime

# Constants
tf2op_url = "http://www.tf2outpost.com/api/core"
tf2op_db = "/var/www/html/tf/tradeid.json"

# Parse tradeid.json
if os.path.exists(tf2op_db):
    with open(tf2op_db) as data_file:    
        trades = json.load(data_file)
else:
    print "Error - please create a tradeid.json file!"
    sys.exit(0)

print datetime.now()

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
