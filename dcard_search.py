import requests, json
from pprint import pprint
import pandas as pd
from collections import defaultdict
from datetime import datetime
import time
import demjson

def parse_page(reqsjson):  
    dict_data = defaultdict(list)
    for i in range(len(reqsjson)):
        dict_data["id"].append(str(reqsjson[i]["id"]))
        dict_data["title"].append(str(reqsjson[i]["title"]))
        dict_data["createdAt"].append(str(reqsjson[i]["createdAt"]))
    df = pd.DataFrame.from_dict(dict_data)
    return df

def reqs_page(url):
    reqs = requests.get(url ,headers = headers)
    reqs.encoding = 'utf8'
    return json.loads(reqs.text)

def first_page(url):
    return parse_page(reqs_page(url))

def other_page(url , index):
    new_url = url + str(index)
    return parse_page(reqs_page(new_url))


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    search = "空氣汙染"
    url = "https://www.dcard.tw/_api/search/posts?highlight=true&query=" + search + "&offset="  
    first_data = first_page(url)
    index = 30
    while not other_page(url , index).empty:
    # print(other_page(url , index))
        other_data = other_page(url , index)
        first_data = pd.concat([first_data , other_data] , ignore_index = True) 
        print(first_data)
        index = index + 30
        time.sleep(5)
    filename ="./" + search + ".csv"
    first_data.to_csv(filename , index = False , encoding="utf_8_sig")

    

    