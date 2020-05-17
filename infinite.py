num_list = []
sum = 0
count = 0
while True:
    num = input("Enter a Number: ")
    if len(num) < 1:break
    try:
        num = int(num)
    except:
        print("Enter a valid number")
        quit()
    sum = sum + num
    count += 1
    num_list.append(num)
print("Sum of the given numbers are: ",sum)
print("Average of the given numbers are: ",sum/count)
print("Largest and Smallest of the given numbers are: ",max(num_list),min(num_list))