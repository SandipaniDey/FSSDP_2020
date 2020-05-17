def translate(s):
    r = ""
    for c in s:
        r += c
        if c in "bcdfghjklmnpqrstvwxz":
            r += 'o' + c
    return r
s = input('Enter Sentemce: ')
print(translate(s))