import string

def main():
    fp = open("input.txt", "r")
    #Remove newline
    line = (fp.readline())[:-1]
    fp.close()

    #Part 1
    print(len(reactPolymers(line)))
    
    #Part 2
    results = {}
    for c in string.ascii_lowercase:
        res = removeElement(line, c)
        res = reactPolymers(res)
        results[c] = res
    
    print(min(len(res) for res in results.values()))

        
def reactPolymers(original):
    res = original[:]
    i = 0
    while i < len(res)-1:
        if ((res[i].isupper() and res[i+1].islower()) or\
           (res[i].islower() and res[i+1].isupper())) and\
           (res[i].lower() == res[i+1].lower()):
            res = res[:i] + res[i+2:]
            #Move backwards to see if it created a new possibility
            if i != 0: i -= 1
        else:
            i += 1
    return res

def removeElement(original, element):
    res = original[:]
    i = 0
    while i < len(res):
        if res[i].lower() == element:
            res = res[:i] + res[i+1:]
        else:
            i += 1   
    return res