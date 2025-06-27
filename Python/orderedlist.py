from collections import OrderedDict
n = int(input())
items = OrderedDict()
for i in range(n):
    line = input().rsplit(' ',1)
    name = line[0]
    price = int(line[1])
    
    if name in items:
        items[name] += price
    else:
        items[name] = price

for name, price in items.items():
    print(name, price)