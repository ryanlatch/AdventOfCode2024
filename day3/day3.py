"""
use regex to sort the instructions from garbage data
process the data (result) + (result)....
"""

import re

with open("input.txt", "r") as file:
    # read the file and remove any leading or trailing whitespace
    text = file.read().strip()
    
# PART 1
# r = raw string, () around just the digits means capture only the digits!
matches = re.findall(r"mul\((\d*),(\d*)\)", text)

total = 0
for match in matches:
    total += int(match[0]) * int(match[1])

print("answer: ", total)

# PART 2
"""
handle do() and don't()
"""

# "?:" groups pattern ('','','') without needing a result 
# | is the OR operator

matchesP2 = re.findall(r"(?:mul\((\d*),(\d*)\))|(do\(\)|don't\(\))", text)

p2total = 0
do=True
for match in matchesP2:
    print(match)
    if "don't()" in match:
        do = False
    if "do()" in match:
        do = True
    # check for the vacant do/dont, meaning its an instruction
    if match[2] == "" and do:
        p2total += int(match[0]) * int(match[1])

print("part 2 answer: ", p2total)
