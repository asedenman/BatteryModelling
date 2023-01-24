#! /usr/bin/env python

import os
import httplib2
import urllib.request, json
import pandas
import raw_data
from dotenv import load_dotenv

load_dotenv()


# These aren't needed, just for this example

from pprint import pformat

def post_elexon(url):
    try:
        http_obj = httplib2.Http()
        resp, content = http_obj.request(
            uri=url,
            method='GET',
            headers={'Content-Type': 'application/xml; charset=UTF-8'},
        )

        print ('===Response===')
        #print (pformat(resp))
        print ('===Content===')
        print (pformat(content))
        print ('===Finished===')
        return content
    except Exception as e:
        print(e)

def main():
    APIKEY = os.getenv("BMREPORTS_APIKEY")
    data = pandas.read_xml(post_elexon(
        url = 'https://api.bmreports.com/BMRS/DERSYSDATA/v1?APIKey=' + APIKEY + '&FromSettlementDate=2023-01-01&ToSettlementDate=2023-01-18&ServiceType=xml'
    ))

if __name__ == "__main__":
    main()