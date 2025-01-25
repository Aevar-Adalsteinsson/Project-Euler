import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_54():
    def is_flush(hand_1,hand_2):
        sort_1 = hand_1[0][1]
        sort_2 = hand_2[0][1]
        flag_1 = True
        flag_2 = True
        for i in range(1,5):
            sort_1i = hand_1[i][1]
            sort_2i = hand_2[i][1]
            if sort_1i != sort_1:
                flag_1 = False
            if sort_2i != sort_2:
                flag_2 = False
        flush_1 = flag_1
        flush_2 = flag_2
        return((flush_1,flush_2))
    def is_straight(rank_1,rank_2,rank):
        low_1 = rank_1[0]
        low_2 = rank_2[0]
        flag_1 = True
        flag_2 = True
        for i in range(1,5):
            rank_1i = rank_1[i]
            rank_2i = rank_2[i]
            if rank_1i != low_1+i:
                if i == 4 and rank_1i == 12 and low_1 == 0:
                    pass
                else:
                    flag_1 = False
            if rank_2i != low_2+i:
                if i == 4 and rank_2i == 12 and low_2 == 0:
                    pass
                else:
                    flag_2 = False
        straight_1 = flag_1
        straight_2 = flag_2
        return((straight_1,straight_2))
    def get_pairs(rank_1,rank_2):
        #all ranks and their multiplicity, one card, pair,trips and quads
        pairs_1 = []
        pairs_2 = []
        
        prev_rank_1 = rank_1[0]
        prev_rank_2 = rank_2[0]
        count_1 = 1
        count_2 = 1
        for i in range(1,5):
            rank_i1 = rank_1[i]
            rank_i2 = rank_2[i]
            if rank_i1 == prev_rank_1:
                count_1 += 1
            else:
                pairs_1.append((count_1,prev_rank_1))
                count_1 = 1
            if rank_i2 == prev_rank_2:
                count_2 += 1
            else:
                pairs_2.append((count_2,prev_rank_2))
                count_2 = 1
            prev_rank_1 = rank_i1
            prev_rank_2 = rank_i2
        pairs_1.append((count_1,prev_rank_1))
        pairs_2.append((count_2,prev_rank_2))
        pairs_1.sort(reverse = True)
        pairs_2.sort(reverse = True)
        return((pairs_1,pairs_2))
        
    f = open("pe_54_poker.txt", "r")

    poker = f.read()
    poker = poker.split("\n")
    poker = poker[:(len(poker)-1)]
    
    rank = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}
    n = len(poker)
    p1_wins = 0
    for i in range(n):
        hands = poker[i]
        hands = hands.split(" ")
        hand_1 = hands[:5]
        hand_2 = hands[5:]
        
        rank_1 = []
        rank_2 = []
        for j in range(5):
            rank_1.append(rank[hand_1[j][0]])
            rank_2.append(rank[hand_2[j][0]])
        rank_1.sort()
        rank_2.sort()
        
        flush_1, flush_2 = is_flush(hand_1,hand_2)
        straight_1, straight_2 = is_straight(rank_1,rank_2,rank)
        pairs_1, pairs_2 = get_pairs(rank_1,rank_2)
        
        #straigt flush and royal flush
        if flush_1 and straight_1:
            if flush_2 and straight_2 and rank_1[4] <= rank_2[4]:
                continue
            p1_wins += 1
            continue
        if flush_2 and straight_2:
            continue
        #four of a kind
        if pairs_1[0][0] == 4:
            if pairs_2[0][0] == 4 and pairs_1[0][1] <= pairs_2[0][1]:
                continue
            p1_wins += 1
            continue
        if pairs_2[0][0] == 4:
            continue
        #full house
        if len(pairs_1) == 2:
            if len(pairs_2) == 2 and pairs_1[0][1] < pairs_2[0][1]:#cant have two three of the kind of the same rank
                continue
            p1_wins += 1
            continue
        if len(pairs_2) == 2:
            continue
        #print("flush")
        #flush
        if flush_1:#can be improved with more rank comparisons
            if flush_2 and rank_1[4] <= rank_2[4]:
                continue
            p1_wins += 1
            continue
        if flush_2:
            continue
        #straight
        if straight_1:
            if straight_2 and rank_1[4] <= rank_2[4]:
                continue
            p1_wins += 1
            continue
        if straight_2:
            continue
        #three of a kind
        if pairs_1[0][0] == 3:
            if pairs_2[0][0] == 3:
                bool_1 = pairs_1[0][1] < pairs_2[0][1]
                bool_2 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] < pairs_2[1][1]
                bool_3 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] == pairs_2[1][1] and pairs_1[2][1] <= pairs_2[2][1]
                if bool_1 or bool_2 or bool_3:
                    continue
                p1_wins += 1
                continue
            else:
                p1_wins += 1
                continue
        if pairs_2[0][0] == 3:
            continue
        #two pairs
        if pairs_1[0][0] == 2 and pairs_1[1][0] == 2:
            if pairs_2[0][0] == 2 and pairs_2[1][0] == 2:
                bool_1 = pairs_1[0][1] < pairs_2[0][1]
                bool_2 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] < pairs_2[1][1]
                bool_3 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] == pairs_2[1][1] and pairs_1[2][1] <= pairs_2[2][1]
                if bool_1 or bool_2 or bool_3:
                    continue
                p1_wins += 1
                continue
            else:
                p1_wins += 1
                continue
        if pairs_2[0][0] == 2 and pairs_2[1][0] == 2:
            continue
        #pair
        if pairs_1[0][0] == 2:
            if pairs_2[0][0] == 2:
                bool_1 = pairs_1[0][1] < pairs_2[0][1]
                bool_2 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] < pairs_2[1][1]
                bool_3 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] == pairs_2[1][1] and pairs_1[2][1] < pairs_2[2][1]
                bool_4 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] == pairs_2[1][1] and pairs_1[2][1] == pairs_2[2][1]
                bool_4 = bool_4 and pairs_1[3][1] <= pairs_2[3][1]
                if bool_1 or bool_2 or bool_3 or bool_4:
                    continue
                p1_wins += 1
                continue
            else:
                p1_wins += 1
                continue
        if pairs_2[0][0] == 2:
            continue
        #high card
        bool_0 = rank_1[4] < rank_2[4]
        bool_1 = rank_1[4] == rank_2[4] and rank_1[3] < rank_2[3]
        bool_2 = rank_1[4] == rank_2[4] and rank_1[3] == rank_2[3] and rank_1[2] < rank_2[2]
        bool_3 = rank_1[4] == rank_2[4] and rank_1[3] == rank_2[3] and rank_1[2] == rank_2[2] and rank_1[1] < rank_2[1]
        bool_4 = rank_1[4] == rank_2[4] and rank_1[3] == rank_2[3] and rank_1[2] == rank_2[2] and rank_1[1] == rank_2[1] and rank_1[0] <= rank_2[0]
        if bool_0 or bool_1 or bool_2 or bool_3 or bool_4:
            continue
        else:
            p1_wins += 1
    return(p1_wins)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_54()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))