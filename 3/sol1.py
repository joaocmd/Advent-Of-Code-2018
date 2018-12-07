import re 

def parseLine(line, matrix, overlaps):
    match = re.search("#(\d*) @ (\d*),(\d*): (\d*)x(\d*)", line)
    nElf = int(match.group(1))
    x = int(match.group(2))
    y = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))
    
    for xi in range(x, x+width):
        for yi in range(y, y+height):
            if (xi, yi) not in matrix:
                matrix[xi, yi] = nElf
            else:
                overlaps[nElf] = True
                if matrix[xi, yi] != -1:
                    overlaps[matrix[xi, yi]] = True
                    matrix[xi, yi] = -1
    
def notOverlapping(overlaps, start, end):
    count = 0
    for i in range(start, end+1):
        if i not in overlaps:
            return i
    return False
            

def main():
    matrix = {}
    overlaps = {}
    
    fp = open("input.txt", "r")
    lines = fp.readlines()
    fp.close()
    
    for line in lines:
        parseLine(line, matrix, overlaps)
    
    print(sum(1 for value in matrix.values() if value == -1))
    print(notOverlapping(overlaps, 1, 1385))