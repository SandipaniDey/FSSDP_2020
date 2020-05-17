import string
str = input('Enter a String: ')
dict = {}
for char in str:
    if char not in string.ascii_lowercase: continue
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] += 1
total = 0
for key, values in dict.items():
    total = values + total
for key,values in dict.items():
    print(key,':',values, int(100*values/total),'%')