import requests
import sys
import json

if len(sys.argv) != 3:
    sys.exit()

try:
    url = f"https://itunes.apple.com/search?entity=song&limit={sys.argv[1]}&term=" + sys.argv[2]
    response = requests.get(url)
    dict_res = response.json()
    # obj = json.dumps(dict_res, indent=2)
    for track in dict_res['results']:
        print(track['trackName'])
except IndexError:
    print('argv list index out of range.')

