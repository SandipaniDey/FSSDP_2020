file = open('absentee.txt','w')
file.close()

with open('absentee.txt','a') as file:
    for i in range(25):
        absenteename = input('Enter Name: ')
        if absenteename =="" :
            break
        file.write(absenteename + "\n")
        
file = open('absentee.txt','r')
print(file.readlines())