"""
Advent of code day 1. sort big list into 2 seperate sorted lists, then get total distances between numbers.
part 2: get a similarity score of format: number * no. of occurences in other list
"""

list1 = []
list2 = []

# read the file 
with open("numbers.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # split the lines by the whitespace and add the list to the list
        num = line.split()
        list1.append(int(num[0]))
        list2.append(int(num[1]))

# sort the lists
list1 = sorted(list1)
list2 = sorted(list2)

# get the total distance between the numbers
totalDistance = 0

for i in range(len(list1)):
    # abs gets the number rather than + or -. Also cast to int as theyre strs
    diff = abs(list1[i] - list2[i])
    totalDistance += diff

print("total distance: ", totalDistance)

# part 2

final_similarity_score = 0

# check every number in the list and * by the amount of times it occurs in the 2nd list
for num in list1:
    final_similarity_score += num * list2.count(num)

print("similarity score: ", final_similarity_score)