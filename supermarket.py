itemlist = {}
while True:
    entry = input('Enter Item name and quantity: ')
    if len(entry) < 1: break
itemname = entry.split()[0:-1]
item = ""
for items in itemname:
    item = item + " " + items
    item = item.strip()
    quantity = int(entry.split()[-1])
    if item not in itemlist:
        itemlist[item] = quantity
    else:
        itemlist[item] += quantity
    
for key,values in itemlist.items():
    print(key,values)