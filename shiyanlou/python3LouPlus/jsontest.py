#! /usr/bin/env python3

import json

data = [ 
    {
        'user_id': 1000,
        'name': 'Shiyan',
        'pass': 10, 
        'study_time': 50, 
    },  
    {   
        'user_id': 2000,
        'name': 'Lou',
        'pass': 15, 
        'study_time': 171,
    }
]

for one in data:
    with open('/tmp/jsontest.json','a') as f:
        f.write(json.dumps(one))
