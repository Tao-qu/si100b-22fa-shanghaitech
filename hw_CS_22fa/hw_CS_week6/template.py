# ===============================---==NOTE: do not use Hardcode==---===============================
# ===============================---==NOTE: do not use Libraries=---===============================


# ========================================TASK1====================================================
# def Act1(PATH: str):
def Act1(hand_card):
    # ====================================YOUR CODE HERE================================================
    order = [i + j for j in ["A", "K", "Q", "J", "T", "9", "8",
                             "7", "6", "5", "4", "3", "2"] for i in ["S", "H", "C", "D"]]
    card_sorted = order[:]
    #hand_card = (",".join(open(PATH).read().split())).split(",")
    for card in order:
        if card in hand_card:
            pass
        else:
            card_sorted.remove(card)
    # print(card_sorted)
    return card_sorted
# ====================================YOUR CODE HERE================================================


# ========================================TASK2====================================================
def Act2():
    # ====================================YOUR CODE HERE================================================
    n, HP = map(int, (" ".join(input().split(","))).split())
    hand_card = (" ".join(input().split(","))).split()
    hand_card = Act1(hand_card)
    cor = {"A": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
           "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13}
    att = []
    for i in range(n):
        att.append(input())

    def Cnum(num_hand, num_att, att_unit, hand_card, HP):
        num_dict = {}
        for key in num_hand:
            num_dict[key] = num_dict.get(key, 0) + 1
        fcount = 0
        for key in sorted([*num_dict]):
            if key > num_att and num_dict[key] >= len(att_unit):
                if key == 14:
                    key = "A"
                elif key == 13:
                    key = "K"
                elif key == 12:
                    key = "Q"
                elif key == 11:
                    key = "J"
                elif key == 10:
                    key = "T"
                else:
                    key = str(key)
                ocount = 0
                olist = []
                while ocount < len(att_unit):
                    ocount += 1
                    if "D"+key in hand_card:
                        olist.insert(0, "D"+key)
                        hand_card.remove("D"+key)
                    elif "C"+key in hand_card:
                        olist.insert(0, "C"+key)
                        hand_card.remove("C"+key)
                    elif "H"+key in hand_card:
                        olist.insert(0, "H"+key)
                        hand_card.remove("H"+key)
                    elif "S"+key in hand_card:
                        olist.insert(0, "S"+key)
                        hand_card.remove("S"+key)
                print(olist)
                break
            else:
                fcount += 1
        if fcount == len(num_dict):
            print("Pass")
            HP -= 1
        return HP

    def Csuit(suit_hand, suit_att, num_hand, num_att, hand_card):
        order = {"S": 3, "H": 2, "C": 1, "D": 0}
        suit_num = []
        for i in range(len(num_hand)):
            if num_hand[i] == num_att:
                suit_num.append(suit_hand[i])
        fcount = 0
        max = 0
        for i in range(len(suit_att)):
            if order[suit_att[i]] > max:
                max = order[suit_att[i]]
        for i in range(len(suit_num)-1, -1, -1):
            if order[suit_num[i]] > max:
                print((suit_num[i]+str(num_att)).split())
                hand_card.remove(suit_num[i]+str(num_att))
                break
            else:
                fcount += 1
        if fcount >= len(suit_num):
            return 1
        else:
            return 0

    for i in range(n):
        if HP > 0 and len(hand_card) > 0:
            att_unit = Act1((" ".join(att[i].split(","))).split())
            suit_att = [att_unit[i][0] for i in range(len(att_unit))]
            num_att = cor[att_unit[0][1]]
            num_att_str = att_unit[0][1]
            suit_hand = [hand_card[i][0] for i in range(len(hand_card))]
            num_hand = []
            for i in hand_card:
                num_hand.append(cor[i[1]])
            if suit_att == ["C", "D"] and "S" + num_att_str in hand_card and "H" + num_att_str in hand_card:
                olist = ["S" + num_att_str, "H" + num_att_str]
                print(olist)
                hand_card.remove("S" + num_att_str)
                hand_card.remove("H" + num_att_str)
            else:
                if len(att_unit) >= 2 or num_att not in num_hand:
                    HP = Cnum(num_hand, num_att, att_unit, hand_card, HP)
                elif len(att_unit) == 0:
                    pass
                else:
                    if Csuit(suit_hand, suit_att, num_hand, num_att, hand_card) == 1:
                        HP = Cnum(num_hand, num_att, att_unit, hand_card, HP)
        else:
            break
    if HP <= 0:
        print("Twisted Fate lost all his HP and lost.")
    else:
        print("Twisted Fate won with "+str(HP)+"HP left.")

# ====================================YOUR CODE HERE================================================


# ========================================TASK3====================================================
def Act3():
    # ====================================YOUR CODE HERE================================================
    n, HP = map(int, (" ".join(input().split(","))).split())
    hand_card = (" ".join(input().split(","))).split()
    hand_card = Act1(hand_card)
    cor = {"A": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
           "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13}
    att = []
    for i in range(n):
        att.append(input())

    def C(n, HP, hand_card, cor, att, att_unit, olist):
        suit_att = [att_unit[i][0] for i in range(len(att_unit))]
        num_att = cor[att_unit[0][1]]
        num_att_str = att_unit[0][1]
        suit_hand = [hand_card[i][0] for i in range(len(hand_card))]
        num_hand = []
        for i in hand_card:
            num_hand.append(cor[i[1]])
        if suit_att == ["C", "D"] and "S" + num_att_str in hand_card and "H" + num_att_str in hand_card:
            olist = ["S" + num_att_str, "H" + num_att_str]
            hand_card.remove("S" + num_att_str)
            hand_card.remove("H" + num_att_str)
            return [HP, olist, hand_card]
        else:
            def Cnum(n, HP, hand_card, cor, att, att_unit, olist, suit_att, num_att, num_att_str, suit_hand, num_hand):
                num_dict = {}
                for key in num_hand:
                    num_dict[key] = num_dict.get(key, 0) + 1
                fcount = 0
                for key in sorted([*num_dict]):
                    if key > num_att and num_dict[key] >= len(att_unit):
                        if key == 14:
                            key = "A"
                        elif key == 13:
                            key = "K"
                        elif key == 12:
                            key = "Q"
                        elif key == 11:
                            key = "J"
                        elif key == 10:
                            key = "T"
                        else:
                            key = str(key)
                        ocount = 0
                        olist = []
                        while ocount < len(att_unit):
                            ocount += 1
                            if "D"+key in hand_card:
                                olist.insert(0, "D"+key)
                                hand_card.remove("D"+key)
                            elif "C"+key in hand_card:
                                olist.insert(0, "C"+key)
                                hand_card.remove("C"+key)
                            elif "H"+key in hand_card:
                                olist.insert(0, "H"+key)
                                hand_card.remove("H"+key)
                            elif "S"+key in hand_card:
                                olist.insert(0, "S"+key)
                                hand_card.remove("S"+key)
                        return [HP, olist, hand_card]
                    else:
                        fcount += 1

                if fcount == len(num_dict):
                    HP -= 1
                    return [HP, olist, hand_card]

            def Csuit(n, HP, hand_card, cor, att, att_unit, olist, suit_att, num_att, num_att_str, suit_hand, num_hand):
                order = {"S": 3, "H": 2, "C": 1, "D": 0}
                suit_num = []
                for i in range(len(num_hand)):
                    if num_hand[i] == num_att:
                        suit_num.append(suit_hand[i])
                fcount = 0
                for i in range(len(suit_num)-1, -1, -1):
                    if order[suit_num[i]] > order[suit_att[0]] and suit_num[i]+num_att_str in hand_card:
                        olist.append(suit_num[i]+num_att_str)
                        hand_card.remove(suit_num[i]+num_att_str)
                        return [HP, olist, hand_card, 0]
                    else:
                        fcount += 1

                if fcount >= len(suit_num):
                    return [HP, olist, hand_card, 1]

            if len(att_unit) >= 2 or num_att not in num_hand:
                temp = Cnum(n, HP, hand_card, cor, att, att_unit, olist,
                            suit_att, num_att, num_att_str, suit_hand, num_hand)
                HP = temp[0]
                olist = temp[1]
                hand_card = temp[2]
                return [HP, olist, hand_card]
            elif len(att_unit) == 0:
                return [HP, olist, hand_card]
            else:
                temp = Csuit(n, HP, hand_card, cor, att, att_unit, olist,
                             suit_att, num_att, num_att_str, suit_hand, num_hand)
                if temp[3] == 1:
                    temp = Cnum(n, HP, hand_card, cor, att, att_unit, olist,
                                suit_att, num_att, num_att_str, suit_hand, num_hand)
                    HP = temp[0]
                    olist = temp[1]
                    hand_card = temp[2]
                    return [HP, olist, hand_card]
                else:
                    HP = temp[0]
                    olist = temp[1]
                    hand_card = temp[2]
                    return [HP, olist, hand_card]

    def C5(n, HP, hand_card, cor, att, att_unit, olist, att_unitb, oflist):
        for i in range(2):
            att_unit = att_unitb[i]
            temp = C(n, HP, hand_card, cor, att, att_unit, olist)
            if HP == temp[0]:
                HP = temp[0]
                olist = temp[1]
                hand_card = temp[2]
                oflist = oflist + olist
            else:
                HP = temp[0]
                olist = temp[1]
                hand_card = Act1(hand_card + olist)
                break
        return [HP, oflist, hand_card]

    for i in range(n):
        if HP > 0 and len(hand_card) > 0:
            att_unit = (" ".join(att[i].split(",")).split())
            olist = []
            if len(att_unit) == 0:
                pass
            elif len(att_unit) == 5:
                def sort5(att_unit):
                    att_unit1 = []
                    att_unit2 = []
                    for i in range(len(att_unit)):
                        if att_unit[i][1] == att_unit[0][1]:
                            att_unit1.append(att_unit[i])
                        else:
                            att_unit2.append(att_unit[i])
                    att_unit1 = Act1(att_unit1)
                    att_unit2 = Act1(att_unit2)
                    if len(att_unit1) == 3:
                        return([att_unit1,att_unit2])
                    else:
                        return([att_unit2,att_unit1])
                
                att_unitb = sort5(att_unit)
                oflist = []
                temp = C5(n, HP, hand_card, cor, att,
                          att_unit, olist, att_unitb, oflist)
                if temp[0] == HP:
                    HP = temp[0]
                    oflist = temp[1]
                    hand_card = temp[2]
                    print(oflist)
                else:
                    hand_card = temp[2]
                    print("Pass")
                    HP -= 1

            else:
                att_unit = Act1(att_unit)
                temp = C(n, HP, hand_card, cor, att, att_unit, olist)
                if temp[0] == HP:
                    HP = temp[0]
                    olist = temp[1]
                    hand_card = temp[2]
                    print(olist)
                else:
                    print("Pass")
                    HP -= 1
        else:
            break
    if HP <= 0:
        print("Twisted Fate lost all his HP and lost.")
    else:
        print("Twisted Fate won with "+str(HP)+"HP left.")
# ====================================YOUR CODE HERE================================================


# ===================================TASK4=========================================================
def Act4():
    # ====================================YOUR CODE HERE================================================
    hand_card = (" ".join(input().split(","))).split()
    suit_card = [hand_card[i][0] for i in range(len(hand_card))]
    num_card = [hand_card[i][1] for i in range(len(hand_card))]
    #print(hand_card, suit_card, num_card)

    def SF(flush):
        n = flush[0]
        cons = 1
        for i in flush:
            if i == n + 1:
                n = i
                cons = cons + 1
                if cons >= 5:
                    break
            else:
                n = i
                cons = 1
        return cons

    suit_dict = {}
    for key in suit_card:
        suit_dict[key] = suit_dict.get(key, 0) + 1
    # print(suit_dict)

    F = 0
    for key in list(suit_dict.keys()):
        value = suit_dict[key]
        #print(key, value)

        if value < 5:
            F += 1
        else:
            flush = []
            for i in range(len(suit_card)):
                if suit_card[i] == key:
                    flush.append(num_card[i])

            for i in range(len(flush)):
                if flush[i] == "A":
                    flush[i] = "1"
                elif flush[i] == "T":
                    flush[i] = "10"
                elif flush[i] == "J":
                    flush[i] = "11"
                elif flush[i] == "Q":
                    flush[i] = "12"
                elif flush[i] == "K":
                    flush[i] = "13"
            flush = list(map(int, flush))
            flush.sort()
            # print(flush)

            if 1 in flush and 13 in flush and 12 in flush and 11 in flush and 10 in flush:
                print("True")
                break
            else:
                cons = SF(flush)
                # print(cons)
                if cons >= 5:
                    print("True")
                    break
                else:
                    F += 1
    if F == len(suit_dict):
        print("False")
# ====================================YOUR CODE HERE================================================


def main():  # DO NOTE DELETE THIS FUNCTION!
    # ==============================================================================
    # Note: if you want oj evaluate your code, uncomment the corresponding function.
    # ==============================================================================

    # Act1("stacked.in")
    # Act2()
    Act3()
    # Act4()
    return 0


if __name__ == '__main__':
    main()
