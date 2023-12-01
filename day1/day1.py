import re
# We need to get the first and last digit of the line
# if there's only one digit it's doubled. 
# can only be 2 dgits

# use regex to remove letters? 


def main():
    file = open("day1.txt", "r")
    lines = file.readlines()
    numbers = []
    for line in lines:
        new_line = stringToNumber(line)
        numbers.append(lineToNumber(new_line))
    print(sum(numbers))



def lineToNumber(line):
    n = re.sub("[a-zA-Z]", '', line)
    return int(str(n[0]) + str(n[-2]))

def stringToNumber(line):
    numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
    words = list(numbers.keys())

    index_min = len(line) + 1
    number_min = ''

    index_max = -1
    number_max = ''
    number_flag = False

    for numb in words:
        index_first = line.find(numb)
        index_last = line.rfind(numb)

        if (index_first == -1 or index_last == -1):
            continue
        number_flag = True

        if (index_first < index_min):
            index_min = index_first
            number_min = numb

        if (index_last > index_max):
            index_max = index_last
            number_max = numb

    
    if (not number_flag):
        return line

    new_line = line[ : index_min] + str(numbers[number_min]) + line[index_min: ]

    if (index_min != index_max):
        index_max += 1
        new_line = new_line[ : index_max] + str(numbers[number_max]) + new_line[index_max: ]

    return new_line


    
if __name__ == "__main__" :
    main()
