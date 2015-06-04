# Bump.tf
Automatically bump TF2Outpost trades

## Usage:

    ./tf2op.py

## Requirements:

Requires a JSON file called `tradeid.json` in the same directory as
`tf2op.py` 

#### Sample:

    [
        {                                                                         
            "uhash":"abcdefg1234567",                           
            "tradeid":[                                                           
                "1234567",                                                       
                "2345678",                                                       
                "3456789",                                                       
                "4567890"                                                        
            ]                                                                     
        }, 
        {                                                                      
            "uhash":"bcdefgh1357924",                                         
            "tradeid":[                                                        
                "1357913",                                                     
                "3579135",                                                     
                "5791357",                                                     
                "7913579"                                                      
            ]                                                                  
        }
    ]

Where `uhash` is your TF2OP cookie and `tradeid` are your individual
trade IDs [can be found in your trade URL]. This script supports
multiple users, so you can have multiple `uhash` values.

## For the site itself:

Requires the Bootstrap [] within `/lib/`
