import re
import numpy

def main():
    file = open("day2.txt", "r")
    lines = file.readlines()
    solution_1(lines)
    solution_2(lines)
    
def solution_1(lines):
    game_limit = {
            "blue":14,
            "red":12,
            "green":13,
            }
    index = 1
    valid_indexs = []
    for line in lines:
        line = parse(line)
        game_maxs = get_max(line)
        if (get_valid_games(game_maxs, game_limit)):
            valid_indexs.append(index)
        index += 1
    print(sum(valid_indexs))


def solution_2(lines):
    powers = []
    for line in lines:
        line = parse(line)
        game_maxs = get_max(line)
        powers.append(numpy.prod(game_maxs))
    print(sum(powers))

    



def parse(line):
    line = re.sub('Game \d+: ', '', line)
    line = line.replace(';', '')
    line = line.replace(',', '')
    line = line.split()
    return line

def get_max(line):
    max_red = 0
    max_green = 0
    max_blue = 0

    current_digit = 0
    current_color = ''

    for part in line:
        if part.isdigit():
            current_digit = int(part)
        else:
            match part:
                case "red":
                    if (current_digit > max_red):
                        max_red = current_digit
                case "green":
                    if (current_digit > max_green):
                        max_green = current_digit
                case "blue":
                    if (current_digit > max_blue):
                        max_blue = current_digit


    return [max_red, max_green, max_blue]

def get_valid_games(game_max, game_limit):
    # order is rgb
    if game_max[0] > game_limit["red"]:
        return False
    if game_max[1] > game_limit["green"]:
        return False
    if game_max[2] > game_limit["blue"]:
        return False
    return True




if __name__ == "__main__":
    main()



# Can use index as game number
#
