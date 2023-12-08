def main():
    file = open("day7_test.txt", "r")
    lines = file.readlines()
    solution_1(lines)
    solution_2(lines)

def solution_1(lines):
    cards = []
    for line in lines:
        cards.append(line.split())
    compare_hands(cards)

    return False

def compare_hands(cards):
    return_cards = []
    for card in cards:
        hand = card[0]
        card.extend(get_hand_type(hand))
    sorted = sort_hands(cards)
    ordered = order_hands(sorted)
#    print(cards)
    return card

def get_hand_type(hand):
    cards_in_hand = [*hand]
    cards_found = dict((x,cards_in_hand.count(x)) for x in set(cards_in_hand))
    # 5 = five of a kind, ... 4,3,2,1. F = full house, H = High card 
    match len(cards_found.values()):
        case 1:
            return '5', 7  # 5 of a kind 
        case 2:
            if (max(cards_found.values()) == 3):
                return '4', 6 # 4 of a kind 
            if (max(cards_found.values()) == 2):
                return 'F', 5 # full house 
        case 3: 
            if (max(cards_found.values()) == 3):
                return '3', 4 # three of a kind
            if (max(cards_found.values()) == 2):
                return '2', 3 # two pair
        case 4:
            return '1', 2 # one pair
        case 5: 
            return 'H', 1 # either nothing or high card

def sort_hands(ranked_hands):
    sorted_hands = [[],[],[],[],[],[],[]]
    for hand in ranked_hands:
        rank = hand[3]
        sorted_hands[rank].append(hand)
    return sorted_hands

def order_hands(input_array):
    for array in input_array:
        if not array:
            continue
        if len(array) < 2:
            continue

        print(array)
    return False

        
def break_ties(input_array):


    return False



    print(cards_in_hand)

def solution_2(lines):
    return False

if __name__ == "__main__" :
    main()
