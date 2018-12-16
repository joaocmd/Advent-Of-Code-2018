import re
import math


class Grid:
        
    def __init__(self, width, heigth, points):
        self.width = width
        self.heigth = heigth
        self.points = points
        
    def safeArea(self, maxDistance):
        region = []
        
        for y in range(0, self.heigth):
            for x in range(0, self.width):
                distances = []
                for point in self.points:
                    distances.append(point.distanceTo(x, y))
                    
                if sum(distances) < maxDistance: region.append([x,y])
                
        return len(region)
    
        
    def largestArea(self):
        areas = {}

        for y in range(0, self.heigth):
            for x in range(0, self.width):
                closest, distance = self.findClosestPoint(x, y)
                if closest != None:
                    pid = closest.getPid()
                    if pid in areas:
                        if x == 0 or y == 0 or x == self.width or y == self.heigth:
                            areas[pid] = math.inf
                        elif areas[pid] != math.inf:
                            areas[pid] += 1
                    else:
                        areas[pid] = 1
        
        largestArea = 0
        for area in areas.values():
            if area != math.inf and area > largestArea: largestArea = area
        
        return largestArea
    
    def findClosestPoint(self, x, y):
        closest = None
        minDistance = None
        valid = True
        for point in self.points:
            distance = point.distanceTo(x, y)
            if minDistance == None:
                minDistance = distance
                closest = point
            elif distance < minDistance:
                valid = True
                minDistance = distance
                closest = point
            elif distance == minDistance:
                valid = False
        
        return (closest, minDistance) if valid else (None, minDistance)
                    
                    
                
    
class Point:
    
    def __init__(self, pid, x, y):
        self.pid = pid
        self.x = x
        self.y = y
        self.area = 0
        
    def getPid(self):
        return self.pid
    
    def distanceTo(self, x, y):
        return abs(self.x - x) + abs(self.y - y)
    
def parseInput(inputLines):
    width = height = 0
    points = []

    pid = 0
    for line in inputLines:
        match = re.search("(\d*), (\d*)", line)
        x = int(match.group(1))
        width = max(x, width)
        y = int(match.group(2))
        height = max(y, height)
        points.append(Point(pid, x, y))
        
        pid += 1
        
    return Grid(width+1, height+1, points)


def main():
    fp = open("input.txt", "r")
    lines = fp.readlines()
    fp.close()
    
    grid = parseInput(lines)
    print(grid.largestArea())
    print(grid.safeArea(10000))
    