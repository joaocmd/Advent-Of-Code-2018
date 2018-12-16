import re
import copy

class Task:
    
    def __init__(self, name, time = 0):
        self.done = False
        self.name = name
        self.dependencies = []
        self.dependants = []
        self.time = time
            
    def getName(self):
        return self.name
    
    def addDependant(self, dependant):
        self.dependants.append(dependant)
    
    def addDependency(self, dependency):
        self.dependencies.append(dependency)    
    
    def isReady(self):
        for task in self.dependencies:
            if not task.isDone():
                return False
        
        return True
    
    def isDone(self):
        return self.done
    
    def finish(self):
        self.done = True
        
    def work(self):
        self.time -= 1
        if self.time <= 0: self.finish()
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __str__(self):
        res = "Tasks "
        for task in self.dependencies:
            res += task.name + " "
        return res + "must be done before " + self.name + " can be completed"

    def __repr__(self):
        return "Task " + self.name + "-" + str(self.time)
        
    
def parseInput(inputlines):
    tasks = {}


    for line in inputlines:
        match = re.search("Step (.) must be finished before step (.) can begin.", line)
        first = match.group(1)
        second = match.group(2)
        
        if first not in tasks:
            tasks[first] = Task(first, time = ord(first) - ord("A") + 61)
        if second not in tasks:
            tasks[second] = Task(second, time = ord(second) - ord("A") + 61)
        
        tasks[first].addDependant(tasks[second])
        tasks[second].addDependency(tasks[first])
    
    return tasks

def calculatePath(original):
    
    def calculatePath_aux(todo):
        ready = []
        for task in todo.values():
            if task.isReady():
                ready.append(task)
                
        ready.sort()
        if len(ready) == 0:
            return ""
        else:
            task = ready[0]
            task.finish()
            todo.pop(task.getName())
            return task.getName() + calculatePath_aux(todo)
    
    tasks = copy.deepcopy(original)
    return calculatePath_aux(tasks)

def printHeader(workers):
    res = "Second   "
    for i in range(0, workers):
        res += "Worker " + str(i+1) + "   "
    print(res)
    
def printSecond(time, workers):
    res = str("%4d"%time) + "        "
    for worker in workers:
        res += "." if worker == None else worker.getName()
        res += "         "
    print(res)

def calculateTime(original, nWorkers):
    printHeader(nWorkers)
    todo = copy.deepcopy(original)
    
    def workInProgress(workers):
        for worker in workers:
            if worker != None:
                return True
        return False
            
    #Initialize workers
    #Each worker has an assigned work
    workers = [None] * nWorkers
    
    time = 0
    while len(todo) != 0 or workInProgress(workers):
  
        #Attend todo tasks
        ready = []
        for task in todo.values():
            if task.isReady():
                ready.append(task)
        ready.sort()
        
        #Assign works to workers
        i = 0
        for w in range(0, nWorkers):
            if i >= len(ready):
                break
            if workers[w] == None:
                task = ready[i]
                workers[w] = task
                todo.pop(task.getName())
                i += 1
                
        printSecond(time, workers)
        #Work current works in progress
        for w in range(0, nWorkers):
            if workers[w] != None:
                workers[w].work()
                if workers[w].isDone():
                    workers[w] = None
        
                   
        time += 1
    printSecond(time, workers)
    return time
        

            
def main():
    fp = open("input.txt") 
    lines = fp.readlines()
    fp.close
    
    tasks = parseInput(lines)
    print(calculatePath(tasks))
    print(calculateTime(tasks, 5))