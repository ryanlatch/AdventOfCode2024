"""
Advent of code day 1. sort big list into 2 seperate sorted lists, then get total distances between numbers.
"""


list1 = []
list2 = []

# read the file 
with open("numbers.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # split the lines by the whitespace and add the list to the list
        num = line.split()
        list1.append(num[0])
        list2.append(num[1])

# sort the lists
list1 = sorted(list1)
list2 = sorted(list2)

# get the total distance between the numbers
totalDistance = 0

for i in range(len(list1)):
    # abs gets the number rather than + or -. Also cast to int as theyre strs
    diff = abs(int(list1[i]) - int(list2[i]))
    totalDistance += diff

print(totalDistance)
