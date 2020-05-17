i=0
my_dict={}
myfile = str(input("Enter the name of the file with .txt extension: "))
with open(myfile,'r') as file :
   file_contents = file.read().split()

   

my_set=set(file_contents)
ListLength=len(file_contents)

my_dict={}
for value in my_set:

    i=0
    j=0
    while(i<ListLength):
       
        if(value==file_contents[i]):
            
            j=j+1
            i=i+1
        else:
            i=i+1
    my_dict[value]=j        

print(my_dict)      