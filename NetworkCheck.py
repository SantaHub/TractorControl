# Checking network 

import urllib2

def internet_check():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1) # Google IP
        return True
    except urllib2.URLError as err: 
        return False