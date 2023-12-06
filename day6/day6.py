import re
import numpy

def main():
    file = open("day6.txt", "r")
    lines = file.readlines()
    solution_1(lines)
    solution_2(lines)

def solution_1(lines):
    data = []
    ways_to_win = []
    for line in lines:
        line = parse(line)
        data.append(line)
    time = [int(t) for t in data[0]]
    distance = [int(d) for d in data[1]]
    for t,d in zip(time, distance):
        ways_to_win.append(get_ways_to_win(t,d))
    print(numpy.prod(ways_to_win))
    return False

def solution_2(lines):
    data = []
    for line in lines:
        line = parse(line)
        data.append(line)
    time = int("".join(data[0]))
    distance = int("".join(data[1])) 
    print(get_ways_to_win(time,distance))
    return False

def get_ways_to_win(time, distance):
    ways_to_win = 0
    increasing = True
    last_distance = 0
    for i in range(time):
        if (not increasing):
            continue
        race_distance = get_distance(time, time - i)
        if (race_distance > distance):
            ways_to_win += 1
        last_distance = race_distance
        if (race_distance < last_distance):
            increasing = False
    return ways_to_win

def get_distance(time, time_pressed):
    return time_pressed * (time - time_pressed)

def parse(line):
    line = re.sub('([A-Z])\w+:\s+', '', line)
    line = line.strip()
    line = line.split()
    return line


if __name__ == "__main__" :
    main()
