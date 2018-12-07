import re
from enum import Enum

class Guard:    
    class Status(Enum):
        AWAKE  = '.'
        ASLEEP = '#' 
    
    class Shift:
        def __init__(self, date, gid):
            self.date = date
            self.gid = gid
            self.hours = [Guard.Status.AWAKE for i in range(0, 60)]
                
        def sleepShift(self, time):
            for i in range(time, 60):
                self.hours[i] = Guard.Status.ASLEEP
                
        def awakeShift(self, time):
            for i in range(time, 60):
                self.hours[i] = Guard.Status.AWAKE
                
        def timeAsleep(self):
            return sum(1 for hour in self.hours if hour == Guard.Status.ASLEEP)
        
        def fillData (self, data):
            for i in range(0, 60):
                if self.hours[i] == Guard.Status.ASLEEP: 
                    data[i] += 1
                      
                
        def __str__(self):
            res = self.date + "  " + "#" + str("%4d" % self.gid) + "  "
            for hour in self.hours:
                res += hour.value
            return res        
            
           
    def __init__(self, gid):
        self.shifts = {}
        self.gid = gid
        
    def getId(self):
        return self.gid
    
    def sleep(self, time, date):
        if date not in self.shifts:
            self.shifts[date] = self.Shift(date, self.gid)
        self.shifts[date].sleepShift(time)

    def awake(self, time, date):
        self.shifts[date].awakeShift(time)
            
    def totalTimeAsleep(self):
        return sum(shift.timeAsleep() for shift in self.shifts.values())
    
    def sleepyTime(self):
        data = [0 for i in range(0, 60)]
        for shift in self.shifts.values():
            shift.fillData(data)
        return data.index(max(data)), max(data)
            
        
    def __str__(self):
        res =  ""
        for shift in self.shifts.values():
            res += str(shift) + "\n"
        return res

def printHeader():
    res =  "Date   ID     Minute\n"
    res += "              "
    for i in range(0, 60):
        res += str(i//10)
    res += "\n              "
    for i in range(0, 60):
        res += str(i%10)
    print(res)

def printGuards(guards):
    guardsList = list(guards)
    guardsList.sort(key = lambda g: g.date)
    for g in guardsList:
        print(g)

def main():
    fp = open("input.txt", "r")
    lines = sorted(fp.readlines())
    fp.close()
    
    guards = {}
    gid = -1
    
    gid = None
    for line in lines:
        match = re.search("\d*-(\d*-\d*) \d*:(\d*)", line)
        date = match.group(1)
        minutes = int(match.group(2))
        
        match = re.search("#(\d*)", line)
        if match:
            gid = int(match.group(1))
            if gid not in guards:
                guards[gid] = Guard(gid)
            continue
        
        match = re.search("wakes up", line)
        if match:
            guards[gid].awake(minutes, date)
            continue
        
        match = re.search("falls asleep", line)
        if match:
            guards[gid].sleep(minutes, date)
            continue
    
    printHeader()
    #part 1
    sleepyGuard = None
    maxSleep = None
    for guard in guards.values():
        if not sleepyGuard:
            sleepyGuard = guard
            maxSleep = guard.totalTimeAsleep()
        elif guard.totalTimeAsleep() > maxSleep:
            sleepyGuard = guard
            maxSleep = guard.totalTimeAsleep()
    
    sleepyTime, _ = sleepyGuard.sleepyTime()
    print(sleepyGuard)
    print(sleepyGuard.getId() * sleepyTime)
    
    #part 2
    sleepyGuard = None
    maxSleepyTime = None
    maxTimes = None
    for guard in guards.values():
        if not sleepyGuard:
            sleepyGuard = guard
            maxSleepyTime, maxTimes = guard.sleepyTime()
        else:
            sleepyTime, nTimes = guard.sleepyTime()
            if nTimes > maxTimes:
                sleepyGuard = guard
                maxSleepyTime = sleepyTime
                maxTimes = nTimes
                
    print(sleepyGuard.getId() * maxSleepyTime)
    