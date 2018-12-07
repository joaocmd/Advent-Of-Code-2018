fp = open("input.txt", "r")
inputs = fp.readlines()
fp.close()

twos = []
threes = []

for line in inputs:
    stringdic = {}
    for l in line:
        if l not in stringdic:
            stringdic[l] = 0
        stringdic[l] += 1
    values = set(stringdic.values())
    if 2 in values:
        twos.append(line)
    if 3 in values:
        threes.append(line)
            
print(len(twos) * len(threes))