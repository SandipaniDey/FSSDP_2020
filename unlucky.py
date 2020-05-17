s = input("Enter Numbers: ").split(",")

p = False
total = 0

for number in s:
    if int(number) == 13:
        p = True
    
    elif not p:
        total += int(number)
    
    elif p and int(number) != 13:
        p = False

print (total)