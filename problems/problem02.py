## 1번
import requests
from pprint import pprint
url = "https://api.bithumb.com/public/ticker/all"
data = requests.get(url).json()['data']

for key in data.keys():
    if type(data[key]) == str:
       continue 
    else:
        change = float(data[key]['max_price']) - float(data[key]['min_price'])   
        if change + float(data[key]['opening_price']) > float(data[key]['max_price']): 
            print(f'{key} 코인은 상승장')
        else:
            print(f'{key} 코인은 하락장')



## 2번

movies = {
    "7번방의선물":12811206,
    "괴물":13019740,

    "국제시장":14257115,
    "극한직업":16261018,
    "도둑들":12983330,
    "명량":17613682,
    "베테랑":13414009,
    "신과함께-죄와벌":14410754,
    "아바타":13624328,
    "어벤져스:엔드게임":13901423,
}

UBD = 172212

for key, value in movies.items():
    if value < UBD * 80:
        print(key)  