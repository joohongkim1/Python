# ## 1.

# def tax(won):
#     if won > 4600:
#         return 1200 * 0.06 + 3400 * 0.15 + (won - 4600) * 0.35
#     elif won >= 1200:
#         return 1200 * 0.06 + (won - 1200) * 0.15
#     else:
#         return won * 0.06

# print(tax(1200))        
# print(tax(4600))
# print(tax(5000))

# ## 2.

# def fee(minute, distance):
#     lent_fee = (minute / 10) * 1200
#     insurance = (minute / 30) * 525
#      
#     if distance > 100:
#         money = 170 * 100 + 85 * (distance - 100) 
#     else:
#         money = distance * 170    
#     return lent_fee + insurance + money

# print(fee(600, 50))
# print(fee(600, 110))


## 3.

# def start_end(words):
#     count = 0
#     for word in words:
#         if len(word) >= 2 and word[0] == word[-1]:
#             count += 1
#     return count

# print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))


## 4. 

# def positive_sum(*numbers):
#     sum = 0
#     for number in numbers:
#         if type(number) == int and number > 0:
#             sum += number
#     return sum

# print(positive_sum(1, -4, 7, 12))
# print(positive_sum(-1, -2, -3, -4))


## 5. 

# def collatz(num):
#     count = 0
#     while num != 1:
#         if count == 500:
#             return -1
#         if num % 2:
#             num = num * 3 + 1
#             count += 1
#         else:
#             num /= 2
#             count += 1
#     return count

# print(collatz(6))
# print(collatz(16))
# print(collatz(27))
# print(collatz(626331))
    

## 6.  

def lonely(numbers):
    










