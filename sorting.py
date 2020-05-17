s = input('Enter Data: ')
lst = [tuple(x.split(',')) for x in s.split()]

print(sorted(lst, key=lambda x: (x[0], x[1], x[2])))