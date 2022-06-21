import json
import requests


def api_request(url):

    response = requests.get(url)
    json_res = json.loads(response.text)

    return json_res

def api_request_raw(url):

    response = requests.get(url)
    json_res = json.dumps(response)

    return json_res
