#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
from requests_oauthlib import OAuth1Session

# read settings
settings = open(os.path.expanduser('~/.throweet.settings'))
CK, CS, AT, AS = map(lambda x: x.strip(), settings.readlines())

# for posting tweets
url = 'https://api.twitter.com/1.1/statuses/update.json'

params = {'status': ' '.join(sys.argv[1:])}

# oauth post
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# check the response
if req.status_code == 200:
    print('succeeded')
else:
    print('Error: {}'.format(req.status_code))
