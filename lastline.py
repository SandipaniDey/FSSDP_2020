fname = str(input("Enter the name of the file with .txt extension: "))
N = 1
with open(fname) as file: 
    for line in (file.readlines() [-N:]): 
        print(line, end ='')			 		