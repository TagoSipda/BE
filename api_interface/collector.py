import requests
import json
from pprint import pprint




url = "http://apis.data.go.kr/1613000/ArvlInfoInqireService/getSttnAcctoArvlPrearngeInfoList"
params = {
    "serviceKey": "BFjPhffz1BsMhNJj/DE2I9niFaznJs1TvecFhI364LBNcv1GJoOThIK1iXBiy2706Qh9Uikac2TvP/OyXg742g==",
    "pageNo": "1",
    "numOfRows": "10",
    "_type": "json",
    "cityCode": "31010",
    "nodeId": "GGB203000287",
}

response = requests.get(url, params=params)
response = json.loads(response.content)
pprint(response)
