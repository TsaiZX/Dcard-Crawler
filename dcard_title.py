import requests, json
from pprint import pprint
import pandas as pd
from collections import defaultdict
from datetime import datetime
import time

def parse_page(reqsjson):  
    dict_data = defaultdict(list)
    for i in range(len(reqsjson)):
        dict_data["id"].append(str(reqsjson[i]["id"]))
        dict_data["title"].append(str(reqsjson[i]["title"]))
        dict_data["school"].append(str(reqsjson[i]["school"]))
        dict_data["createdAt"].append(str(reqsjson[i]["createdAt"]))
    df = pd.DataFrame.from_dict(dict_data)
    old_url = get_old_url(df)
    return(df , old_url)
    
def get_old_url(df):
    old_url="https://www.dcard.tw/_api/forums/trending/posts?popular=false&before="
    return(old_url +  str(df["id"][len(df)-1]))

def get_first_page(heasers):
    new_url="https://www.dcard.tw/_api/forums/trending/posts?popular=false"
    reqs = requests.get(new_url ,headers = headers)
    reqsjson = json.loads(reqs.text)
    # pprint(reqsjson)
    first_data , old_url = parse_page(reqsjson)
    return first_data , old_url

def get_old_page(headers , old_url):
    
    reqs = requests.get(old_url ,headers = headers)
    reqsjson = json.loads(reqs.text)
    parse_data , old_url = parse_page(reqsjson)
    return parse_data , old_url
    

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    first_data , old_url = get_first_page(headers)

    # first_data = pd.read_csv("./title.csv")
    # print(first_data)
    # old_url = "https://www.dcard.tw/_api/forums/trending/posts?popular=false&before=229760331"  


    end_time =  datetime.strptime("2018-07-01T00:00:00.0000Z" , '%Y-%m-%dT%H:%M:%S.%fZ')
    last_time = datetime.strptime(first_data["createdAt"][len(first_data) - 1], '%Y-%m-%dT%H:%M:%S.%fZ')

    while  end_time < last_time :
        old_data , old_url = get_old_page(headers , old_url)
        last_time = datetime.strptime(old_data["createdAt"][len(old_data) - 1], '%Y-%m-%dT%H:%M:%S.%fZ')
        first_data = pd.concat([first_data , old_data] , ignore_index = True) 
        print(first_data)
        time.sleep(1)
    # first_data.to_csv("title.csv" , index = False , encoding="utf_8_sig")
    


    
    
   

    