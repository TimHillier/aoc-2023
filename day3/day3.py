def main():
    file = open("day3.txt", "r")
    lines = file.readlines()
    solution_1(lines)
    solution_2(lines)

def solution_1(lines):
    line_length = len(lines[0].strip())
    full_line = "".join(line.strip() for line in lines)
    symbol_indexs = [index for index, character in enumerate(full_line) if character in ['#', '*', '$', '+', '@', '/', '%', '&', '=', '-']]
    valid_indexs = get_indexs(full_line, symbol_indexs, line_length)
    numbers = search_string_for_numbers(full_line, valid_indexs)
    print(sum(numbers))
    return False

def get_indexs(full_line, symbol_indexs, line_length):
    valid_indexs = []
    for symbol in symbol_indexs:
        valid_indexs = valid_indexs + get_valid_locations(symbol, line_length)
    return set(valid_indexs)

def nearby(full_line, symbol_index):


    return how_many

def search_string_for_numbers(full_line, valid_indexs):
    searched_indexs = []
    found_numbers = []

    for index in valid_indexs:

        if (index in searched_indexs):
            continue

        searched_indexs.append(index)

        if (full_line[index].isdigit()):
            # move left to find start of number:
            left = index
            while full_line[left].isdigit():
                left -= 1
            left += 1
            number = ''
            while full_line[left].isdigit():
                searched_indexs.append(left)
                number = number + full_line[left]
                left += 1
            found_numbers.append(int(number))
    return found_numbers

def get_valid_locations(symbol_index, line_length):
    d = symbol_index - 1 # 13 - 1 = 12 
    e = symbol_index + 1 # 13 + 1 = 14
    a = d - line_length # 12 - 10 = 2
    b = symbol_index - line_length # 13 - 10 = 3
    c = e - line_length # 14 - 10 = 4
    f = d + line_length # 12 + 10 = 22
    g = symbol_index + line_length # 13 + 10 = 23
    h = e + line_length # 14 + 10 = 24

    return [a,b,c,d,e,f,g,h]


def solution_2(lines):
    line_length = len(lines[0].strip())
    full_line = "".join(line.strip() for line in lines)
    symbol_indexs = [index for index, character in enumerate(full_line) if character in ['*']]
    ratios = []
    for symbol in symbol_indexs:
        valid_indexs = get_valid_locations(symbol, line_length)
        numbers = search_string_for_numbers(full_line, valid_indexs)
        if (len(numbers) == 2):
            ratios.append(numbers[0] * numbers[1])
    print(sum(ratios))
    
    return False

if __name__ == "__main__" :
    main()
