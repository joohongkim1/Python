## 1.

import requests
from pprint import pprint

url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']
pprint(data)

max_price = int(data.get('max_price'))
min_price = int(data.get('min_price'))

price_range = max_price - min_price

opening_price = int(data.get('opening_price'))

if opening_price + price_range > max_price:
    print('상승장')
else:
    print('하락장')

## 2.

# 여기에 코드를 작성하세요
phone = input()

try:
    numbers = [int(number) for number in phone]
except:
    print('핸드폰 번호를 입력하세요')
else:
    if phone[0:3] == '010' and len(phone) == 11:
        result = '*' * 7 + phone[-4:]
        print(result)
    else:
        print('핸드폰 번호를 입력하세요')

## 3.

# 여기에 코드를 작성하세요
text = input()
num = len(text) // 2

if len(text) % 2:
    middle = text[num]
else:
    middle = text[num-1:num+1] 
    
print(middle)