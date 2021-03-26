import jieba
list(jieba.cut('ok thanks'))

price = input("Input the stock price of Apple: ")
print(type(price))
print(price)

price = eval(input("Input the stock price of Apple: "))
print(type(price))
print(price)
