import math
# basic input info.
labels = ['Python', 'Java', 'JavaScript', 'C#', 'PHP']
data = [29.9, 19.1, 8.2, 7.3, 6.2]

# determine largest data feilds.
biggest_data = data[0]
lowest_data = data[0]
x = 1
if data[x] > biggest_data:
    biggest_data = data[x]
if data[x] < lowest_data:
    lowest_data = data[x]
x = x + 1
if data[x] > biggest_data:
    biggest_data = data[x]
if data[x] < lowest_data:
    lowest_data = data[x]
x = x + 1
if data[x] > biggest_data:
    biggest_data = data[x]
if data[x] < lowest_data:
    lowest_data = data[x]
x = x + 1
if data[x] > biggest_data:
    biggest_data = data[x]
if data[x] < lowest_data:
    lowest_data = data[x]
    
# determine bar length.
bar_length = math.floor(biggest_data) + 11

# fix label lengths
x = 0
if len(labels[x]) >= 8:
    labels[x] = labels[x][0:8]
x = x + 1
if len(labels[x]) >= 8:
    labels[x] = labels[x][0:8]
x = x + 1
if len(labels[x]) >= 8:
    labels[x] = labels[x][0:8]
x = x + 1
if len(labels[x]) >= 8:
    labels[x] = labels[x][0:8]
x = x + 1
if len(labels[x]) >= 8:
    labels[x] = labels[x][0:8]

# final print statements
x = 0
print("-" * bar_length)
print(labels[x], " " * (9 - len(labels[x])), ": ", "=" * math.floor(data[x]), sep="")
x = x + 1
print(labels[x], " " * (9 - len(labels[x])), ": ", "=" * math.floor(data[x]), sep="")
x = x + 1
print(labels[x], " " * (9 - len(labels[x])), ": ", "=" * math.floor(data[x]), sep="")
x = x + 1
print(labels[x], " " * (9 - len(labels[x])), ": ", "=" * math.floor(data[x]), sep="")
x = x + 1
print(labels[x], " " * (9 - len(labels[x])), ": ", "=" * math.floor(data[x]), sep="")
x = x + 1
print("-" * bar_length)
print("min:", "{:.2f}".format(lowest_data), "max:", "{:.2f}".format(biggest_data))
