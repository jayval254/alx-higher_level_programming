#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response."""
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as res:
        header_var = res.getheader('X-Request-Id')
        print(header_var)
