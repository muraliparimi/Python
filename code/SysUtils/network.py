#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost

def check_connectivity():
    request = requests.get("http://www.google.com")
    return request
