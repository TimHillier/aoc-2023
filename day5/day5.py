import re

def main():
    file = open("day5_test.txt", "r")
    lines = file.readlines() # array
    solution_1(lines)
    solution_2(lines)

def solution_1(lines):
    almanac = []
    for line in lines:
        almanac.append(parse(line))
    alm_arr = get_mapping(almanac)
    seeds = alm_arr.pop(0)[0]
    get_location(seeds,alm_arr)
    return False

def solution_2(lines):
    almanac = []
    for line in lines:
        almanac.append(parse(line))
    alm_arr = get_mapping(almanac)
    seeds = alm_arr.pop(0)[0]
    seed_pairs = [[int(seeds[i]), int(seeds[i+1])] for i in range(0, len(seeds) - 1, 2)]
    get_location_range(seed_pairs, alm_arr)
    return False

def parse(line):
    line = re.sub('([a-zA-Z])*(-)*(:)*(,)*', '', line)
    # split lines by " " 
    if(line == ' \n'):
        return None 
    line = line.strip()
    line = line.split(' ')
    return line

def get_location_range(seed_ranges, alm_arr):
    next = seed_ranges
########    for section in alm_arr:
    low = get_next_range(next, alm_arr)
    print(min(next))
    return False

def get_next_range(seed_ranges, sections):
    lowest = -1
    for array in seed_ranges:
        seed_start = array[0]
        seed_stop = array[1]
        for seed in range(seed_start, (seed_start + seed_stop)):
            #            print("Testing Seed: " + str(seed))
            next = [seed]
            for section in sections:
                next = get_next(next, section)

#            print("Location: " + str(next))
            if (lowest == -1):
                lowest = next 
                continue
            if (lowest > next):
                lowest = next 
                continue

    print("Lowest: " + str(lowest))
    return False


def get_mapping(almanac):
    alm_arr = []
    section = []
    for element in almanac: 
        if element == None:
            alm_arr.append(section)
            section = []
            continue
        if element == ['']:
            continue
        section.append(element)
    alm_arr.append(section)
    return alm_arr

def get_location(seeds, alm_arr):
    next = seeds
    for section in alm_arr:
        next = get_next(next, section)
    print(min(next))
    return False

def get_next(seeds, section):
    next_seeds = []
    seeds = list(map(int,seeds))
    for array in section:
        source_start = int(array[1])
        source_end = source_start + int(array[2]) - 1
        destination_start = int(array[0])
        found_seeds = []
        for seed in seeds:
            if(seed >= source_start and seed <= source_end):
                seed_index = seed - source_start
                next_seeds.append(destination_start + seed_index)
                found_seeds.append(seed)
        seeds = [x for x in seeds if x not in found_seeds]
    return next_seeds + seeds

if __name__ == "__main__" :
    main()
