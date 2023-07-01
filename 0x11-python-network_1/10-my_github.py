#!/usr/bin/python3
"""takes your GitHub credentials, and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import sys
    import requests

    url = 'https://api.github.com/user'

    username = sys.argv[1]
    token = sys.argv[2]

    req = requests.get(url, auth=(username, token))
    print(req.json().get("id"))
