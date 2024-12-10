
with open("input.txt", "r") as file:
    # read the file and remove any make it a list of strings essentially making a grid
    instruc = file.read().splitlines()

# handle the rules and updates in to seperate lists
rules = []
updates = []
for inst in instruc:
    if "|" in inst:
        new = inst.split(sep="|")
        for i in range(len(new)):
            new[i] = int(new[i])
        rules.append(new)
    elif "," in inst:
        new = inst.split(sep=",")
        for i in range(len(new)):
            new[i] = int(new[i])
        updates.append(new)
# print(updates)
# print(rules)

# check each update by looking for the rules
# check each updates position i.e. 75 against every instance of that
# that number in the rules
# check to see if that number is in the right position by checking
# every rule against the update.
# if it passes move on, if not break.


def checkOrder(update, rules):
# check if both the numbers in the rule appear in the update
    for x, y in rules:
        if x in update and y in update:
            # get the index of x and y 
            x_index = update.index(x)
            y_index = update.index(y)
            if x_index > y_index:
                return False
    return True
                
# get the middle page, len()
mid = []

for update in updates:
    if checkOrder(update, rules):
        # if it is correctly ordered, get the middle page
        mid_page = update[len(update) // 2]
        mid.append(mid_page)

# add up all middle pages
print("part 1: ", sum(mid))

# part 2

# get the incorrect updates
# order them correctly
# sum the middle of the incorrect updates 


def checkOrder(update, rules):
# check if both the numbers in the rule appear in the update
    for x, y in rules:
        if x in update and y in update:
            # get the index of x and y 
            x_index = update.index(x)
            y_index = update.index(y)
            if x_index > y_index:
                return True
    return False

def changeOrder(update, rules):
    
    
    return 
# get the middle page, len()
mid = []

for update in updates:
    if checkOrder(update, rules):
        new_update = changeOrder(update,rules)
        # if it is correctly ordered, get the middle page
        mid_page = new_update[len(new_update) // 2]
        mid.append(mid_page)

                