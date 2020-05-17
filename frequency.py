test_str = input('Enter Data: ')
all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
  

print ("Count of given data is : "+  str(all_freq)) 