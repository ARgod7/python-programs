from collections import Counter


def solution(cards):
    card_values = { '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 'J':10, 'Q':11, 'K':12, 'A':13}
    rank_counter = Counter()
    suit_counter = Counter()
    card_dict = {}
    for card in cards:
        rank = card[:-1]
        rank_counter[rank] += 1
        suit = card[-1]
        suit_counter[suit] += 1
        card_dict[card] = (rank,suit)
    single = []
    for rank,count in sorted(rank_counter.items()):
        if count == 1:
            single.append(rank)
    return 
solution(["AS","10S","10H","8S","8D","QD"])