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
    next_range = seed_ranges
    for section in alm_arr:
        print("Next Range: " + str(next_range))
        print("Next Section: " + str(section))
        next_range = get_next_range(next_range, section)
    print(min(next_range))

def get_next_range(seed_ranges, sections):
    # return an array of [[start_value, range]...]
    next_range = []
    # find start
#    print(seed_ranges)
#    print(sections)

    for seed_range in seed_ranges:
        range_start = seed_range[0]
        range_end = range_start + seed_range[1] - 1
        for array in sections:

            source_start = int(array[1])
            source_end = source_start + int(array[2]) - 1
            destination_start = int(array[0])
            destination_end = destination_start + int(array[2]) - 1

            '''
            if(source_start > range_start or source_end < range_start):
                continue
            if(destination_start > range_end or destination_end < range_end):
                continue
            '''

            new_range_start_index = range_start - source_start
            new_range_start = destination_start + new_range_start_index

            left_over = 0 

            if(new_range_start + seed_range[1] - 1 > destination_end):
                new_range_range = new_range_start - destination_end
                left_over = seed_range[1] - new_range_range
            else:
                new_range_range = seed_range[1]

            add_range = [new_range_start, new_range_range]
            print("Add_range: " + str(add_range))


            next_range.append([new_range_start, new_range_range])

            if(left_over > 0):
                #append to seed_ranges
                seed_ranges.append[range_end - left_over, left_over]

            '''
            print("New Range Start: " + str(new_range_start))
            print("Source_start: " + str(source_start))
            print("Source_end: " + str(source_end))
            print("Destination_start: " + str(destination_start))
            print("Destination_end: " + str(destination_end))
            print("Range_start: " + str(range_start))
            print("Range_end: " + str(range_end))
            '''
    return next_range

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

def get_location(seeds, alm_arr):
    next = seeds
    for section in alm_arr:
        next = get_next(next, section)
    print(min(next))
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



if __name__ == "__main__" :
    main()
