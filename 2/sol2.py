def compareWords(main, other):
    length = len(main)
    differences = {}
    for i, l in enumerate(main):
        if l != other[i]:
            differences[i] = 1
            if len(differences) > 1:
                return
    
    if len(differences) == 1:
        diff_index = list(differences.keys())[0]
        print(f"main  : {main}", end = "")
        print(f"other : {other}", end = "")
        print(f"diff  : {diff_index*'-'}^")
        common = main[0:diff_index] + main[diff_index+1:]
        print(f"common: {common}")


def main():
    fp = open("input.txt", "r")
    inputs = fp.readlines()
    fp.close()
    
    for i, word in enumerate(inputs):
        j = i + 1
        rest = inputs[j:]
        for other in rest:
            compareWords(word, other)