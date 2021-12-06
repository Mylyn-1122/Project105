import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
def mean(data):
    dataLength = len(data)
    total_amount = 0
    for x in data:
        total_amount+=int(x)
    mean = total_amount/dataLength
    return mean

list = []
for number in data: 
    a = int(number)-mean(data)
    a = a**2
    list.append(a)

sum = 0
for i in list:
    sum = sum+i

result = sum/(len(data)-1)
std = math.sqrt(result)
print(std)