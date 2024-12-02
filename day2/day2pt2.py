"""
safe reports if BOTH are true:
- all increasing / decreasing
- any 2 adjacent levels differ by 1-3

pt 2:
allowed one mistake!
"""

# handle the data
levels_data = []
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        level = line.split()
        for i in range(len(level)):
            level[i] = int(level[i])
        levels_data.append(level)

# part 2
def is_safe(level):
    # check if the level and the sorted list is the same
    if level == sorted(level):
        check1_pass = True
    # also in reverse
    elif level == sorted(level, reverse=True):
        check1_pass = True
    else:
        check1_pass = False
    
    allowed_diff = [1, 2, 3]
    # assume true until proven otherwise
    check2_pass = True
    if check1_pass:
        for i in range(len(level) - 1):
            # when bigger diff found, check fails
            if abs(level[i] - level[i+1]) not in allowed_diff:
                check2_pass = False
                break
    
    if check1_pass and check2_pass:
        return True
    

actually_safe = 0

for level in levels_data:
    # if its already safe, we can add it to the list
    if is_safe(level):
        actually_safe += 1
        continue

    # check the lists by removing an entry from each level, except first and last number
    for i in range(len(level)):
        modified_level = level[:i] + level[i+1:]
        # check that modified level
        if is_safe(modified_level):
            actually_safe += 1
            break

print(actually_safe)
            

