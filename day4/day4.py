import re

def main():
    file = open("day4.txt", "r")
    lines = file.readlines()
    solution_1(lines)
    solution_2(lines)

def solution_1(lines):
    score = []
    for line in lines:
        line = parse(line)
        score.append(calc_score(line))
    print(sum(score))
    return False

def solution_2(lines):
    number_of_cards = [1] * len(lines)
    for index, line in enumerate(lines):
        line = parse(line)
        wins = len(get_wins(line))
        current_index = index + 1
        for w in range(wins):
            number_of_cards[current_index] += number_of_cards[index]
            current_index += 1

    print(sum(number_of_cards))
    return False

def calc_score(game):
    same = get_wins(game)
    score = int(pow(2, len(same)-1))
    return score

def get_wins(game):
    same = list(set(game[0]) & set(game[1]))
    return same
    

def parse(line):
    line = re.sub('Card \d+: ', '', line)
    line = line.strip()
    line = line.split('|')
    line[0] = line[0].split()
    line[1] = line[1].split()
    return line

if __name__ == "__main__" :
    main()
