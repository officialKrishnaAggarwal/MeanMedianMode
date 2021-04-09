import csv
with open('height-weight.csv', newline='') as f:
    read = csv.reader(f)
    file_data = list(read)
file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))
n = len(new_data)
new_data.sort()

if n % 2 == 0:
    med1 = float(new_data[n//2])
    med2 = float(new_data[n//2-1])
    median = (med1 + med2)/2
else:
    median = new_data[n//2]
print("Median is:" + str(median))
