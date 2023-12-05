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
    return False

def parse(line):
    line = re.sub('([a-zA-Z])*(-)*(:)*(,)*', '', line)
    # split lines by " " 
    if(line == ' \n'):
        return None 
    line = line.strip()
    line = line.split(' ')
    return line

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
        next = get_next(next, section) # I think this is the part that loops.
        print(next)
    print(min(next))
    return False

def get_next(seeds, section):
    next_seeds = []
    for array in section:
        source_start = int(array[1])
        source_end = source_start + int(array[2]) - 1
        destination_start = int(array[0])
        destination_end = destination_start+ int(array[2]) - 1

        found_seeds = []
        for seed in seeds:
            seed = int(seed)
            if(seed >= source_start and seed <= source_end):
                print(seed - source_start)
                seed_index = seed - source_start
                next_seeds.append(destination_start + seed_index)
                found_seeds.append(seed)

        diff_seeds = list((set(list(map(int, seeds))) - set(found_seeds)))
        return next_seeds + diff_seeds



#        rejected_seeds = []
#       found_seeds = []
#       for seed in seeds:
#           seed = int(seed)
#           if(seed in source_array):
#               found_seeds.append(seed)
#               next_seeds.append(destination_array[source_array.index(seed)])


if __name__ == "__main__" :
    main()
