import csv

with open('zoo.csv','rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    total_water_needed = 0
    # Use the below line to skip the header line from the csv file 
    next(csv_reader) 
    for column in csv_reader:
        total_water_needed = int(column[2])+total_water_needed

print ("Total water needed by all the animals : "+str(total_water_needed))
