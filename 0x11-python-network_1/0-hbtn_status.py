#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status """
if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        this = response.read()
        print("Body response:")
        print("\t- type:", this.__class__)
        print("\t- content:", this)
        print("\t- utf8 content:", this.decode("utf-8"))
