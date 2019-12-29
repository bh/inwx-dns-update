#!/usr/bin/env python

import os
import pprint

import requests
from dotenv import load_dotenv
from INWX.Domrobot import ApiClient


def get_public_ip():
    return requests.get('http://ip.42.pl/raw').text


def main():
    load_dotenv()

    my_ip = get_public_ip()
    api_client = ApiClient(api_url=ApiClient.API_LIVE_URL, debug_mode=False)
    api_client.login(os.getenv("INWX_USERNAME"), os.getenv("INWX_PASSWORD"))

    result = api_client.call_api("nameserver.updateRecord", method_params={"type": "A", "name": os.getenv(
        "RECORD_NAME"), "content": my_ip, "id": os.getenv("RECORD_ID"), "ttl": 300})
    pprint.pprint(result)   

if __name__ == '__main__':
    main()
