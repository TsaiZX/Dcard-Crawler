import pandas as pd
import demjson
import requests, json
import time
from collections import defaultdict

def load_id(path):
    data = pd.read_csv(path , encoding = 'utf-8')
    return data["id"]

def req_page(id , headers):
    url = "https://www.dcard.tw/_api/posts/" + str(id)
    reqs = requests.get(url , headers = headers)
    reqs.encoding = 'utf8'
    return json.loads(reqs.text)

def parse_page(page_detail , dict_data):
    dict_data["id"].append(str(page_detail["id"]))
    dict_data["title"].append(str(page_detail["title"]))
    dict_data["content"].append(str(page_detail["content"]))
    dict_data["createdAt"].append(str(page_detail["createdAt"]))
    return dict_data

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    datapath = "./air.csv" 
    data_id = load_id(datapath)
    dict_data = defaultdict(list)

    for i in data_id:
        try:
            page_detail = req_page(i , headers)
            dict_data = parse_page(page_detail , dict_data)
            print(i)
            time.sleep(1)
        except:
            pass
    print(dict_data)
    df = pd.DataFrame.from_dict(dict_data)
    df.to_csv("./"+ datapath + "_detail.csv" , index = False , encoding="utf_8_sig")


    
