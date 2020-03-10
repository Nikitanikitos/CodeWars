class PokerHand:
    RESULT = ["", "Loss", "Tie", "Win"]
    ORDER = "A23456789AJKQT"
    PRIORITY = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, hand):
        self.hand = hand

    def new_hand(self, hand):
        cards = suit = total = ""
        hand = hand.replace(' ', '')
        for i, char in enumerate(hand):
            if i % 2 == 0:
                cards += char
            else:
                suit += char
        for c in sorted(cards):
            total += c
        return f'{total} {suit}'

    def check(self, hand, other):
        if hand == other:
            return 2
        elif self.PRIORITY[hand[0]] > self.PRIORITY[other[0]] or self.PRIORITY[hand[1]] > self.PRIORITY[other[1]]:
            return 3
        else:
            return 1

    def highest_kicker(self, hand, other, n):
        kicker1 = kicker2 = 0
        for c, q in zip(hand, other):
            if self.PRIORITY[c] > kicker1 and hand.count(c) <= n: kicker1 = self.PRIORITY[c]
            if self.PRIORITY[q] > kicker2 and hand.count(q) <= n: kicker2 = self.PRIORITY[q]
        if kicker1 > kicker2:
            return 3
        elif kicker1 < kicker2:
            return 1
        else:
            return 2

    def flash_royal(self, hand):
        hand, q = hand.split()
        return hand in "AJKQT" and q.count(q[0]) == 5

    def street_flash(self, hand, other):
        hand, q = hand.split()
        other, k = other.split()
        if hand in self.ORDER and q.count(q[0]) == 5 and other in self.ORDER and k.count(k[0]) == 5:
            return self.highest_kicker(hand, other, 1)
        elif hand in self.ORDER and q.count(q[0]) == 5:
            return 3
        elif other in self.ORDER and k.count(k[0]) == 5:
            return 1
        return 0

    def four_cards(self, hand, other):
        hand, q = hand.split()
        other, k = other.split()
        if hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4 and other.count(other[0]) == 4 or other.count(
                other[1]) == 4:
            if self.PRIORITY[hand[0]] == self.PRIORITY[other[0]] or self.PRIORITY[hand[1]] == self.PRIORITY[other[1]]:
                return self.highest_kicker(hand, other, 1)
            elif self.PRIORITY[hand[0]] > self.PRIORITY[other[0]] or self.PRIORITY[hand[1]] > self.PRIORITY[other[1]]:
                return 3
            elif self.PRIORITY[hand[0]] < self.PRIORITY[other[0]] or self.PRIORITY[hand[1]] < self.PRIORITY[other[1]]:
                return 1
        elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
            return 3
        elif hand.count(other[0]) == 4 or hand.count(other[1]) == 4:
            return 1
        else:
            return 0

    def full_house(self, hand, other):
        res1 = res2 = 0
        hand, q = hand.split()
        other, k = other.split()
        for c, q in zip(hand, other):
            if hand.count(c) == 3 or hand.count(c) == 2: res1 += 1
            if hand.count(q) == 3 or hand.count(q) == 2: res2 += 1
        if res1 == res2 == 5:
            return self.check(hand, other)
        elif res1 == 5:
            return 3
        elif res2 == 5:
            return 1
        return 0

    def flash(self, hand, other):
        hand, q = hand.split()
        other, k = other.split()
        if q.count(q[0]) == 5 and k.count(k[0]) == 5:
            return self.highest_kicker(hand, other, 1)
        elif q.count(q[0]) == 5:
            return 3
        elif k.count(k[0]) == 5:
            return 1
        return 0

    def street(self, hand, other):
        hand, k = hand.split()
        other, k = other.split()
        if hand in self.ORDER and other in self.ORDER:
            return self.highest_kicker(hand, other, 1)
        elif hand in self.ORDER:
            return 3
        elif other in self.ORDER:
            return 1
        return 0

    def three_cards(self, hand, other):
        hand, k = hand.split()
        other, k = other.split()
        res1 = res2 = 0
        for c, q in zip(hand, other):
            if hand.count(c) == 3: res1 += 1
            if other.count(q) == 3: res2 += 1
        if res1 == res2 == 3:
            return self.highest_kicker(hand, other, 1)
        elif res1 == 3:
            return 3
        elif res2 == 3:
            return 1
        return 0

    def two_pairs(self, hand, other):
        hand, k = hand.split()
        other, k = other.split()
        res1 = res2 = 0
        for c, q in zip(hand, other):
            if hand.count(c) == 2: res1 += 1
            if other.count(q) == 2: res2 += 1
        if res1 == res2 == 4:
            return self.highest_kicker(hand, other, 1)
        elif res1 == 4:
            return 3
        elif res2 == 4:
            return 1
        return 0

    def pair(self, hand, other):
        hand, k = hand.split()
        other, k = other.split()
        res1 = res2 = 0
        for c, q in zip(hand, other):
            if hand.count(c) == 2: res1 += 1
            if other.count(q) == 2: res2 += 1
        if res1 == res2 == 2:
            return self.check(hand, other)
        elif res1 == 2:
            return 3
        elif res2 == 2:
            return 1
        return 0

    def kicker(self, hand, other):
        hand, k = hand.split()
        other, k = other.split()
        return self.highest_kicker(hand, other, 1)

    def compare_with(self, other):
        self.hand = self.new_hand(self.hand)
        other = self.new_hand(other)

        if self.hand == other:
            return self.RESULT[2]
        elif self.flash_royal(self.hand):
            return self.RESULT[3]
        elif self.flash_royal(other):
            return self.RESULT[1]
        elif x:= self.street_flash(self.hand, other):
            return self.RESULT[x]
        elif x:= self.four_cards(self.hand, other):
            return self.RESULT[x]
        elif x:= self.full_house(self.hand, other):
            return self.RESULT[x]
        elif x:= self.flash(self.hand, other):
            return self.RESULT[x]
        elif x:= self.street(self.hand, other):
            return self.RESULT[x]
        elif x:= self.three_cards(self.hand, other):
            return self.RESULT[x]
        elif x:= self.two_pairs(self.hand, other):
            return self.RESULT[x]
        elif x:= self.pair(self.hand, other):
            return self.RESULT[x]
        elif x:= self.kicker(self.hand, other):
            return self.RESULT[x]
        else: return self.RESULT[2]


# loss
player1 = PokerHand("2H 3H 4H 5H 6H")
print(player1.compare_with("KS AS TS QS JS"))
# win
player2 = PokerHand("2H 3H 4H 5H 6H")
print(player2.compare_with("AS AD AC AH JD"))
# win
player3 = PokerHand("AS AH 2H AD AC")
print(player3.compare_with("JS JD JC JH 3D"))
# loss
player4 = PokerHand("2S AH 2H AS AC")
print(player4.compare_with("JS JD JC JH AD"))
# win
player5 = PokerHand("2S AH 2H AS AC")
print(player5.compare_with("2H 3H 5H 6H 7H"))
# win
player6 = PokerHand("AS 3S 4S 8S 2S")
print(player6.compare_with("2H 3H 5H 6H 7H"))
# win
player7 = PokerHand("2H 3H 5H 6H 7H")
print(player7.compare_with("2S 3H 4H 5S 6C"))
# tie
player8 = PokerHand("2S 3H 4H 5S 6C")
print(player8.compare_with("3D 4C 5H 6H 2S"))
# win
player9 = PokerHand("2S 3H 4H 5S 6C")
print(player9.compare_with("AH AC 5H 6H AS"))
# loss
player10 = PokerHand("2S 2H 4H 5S 4C")
print(player10.compare_with("AH AC 5H 6H AS"))
# win
player11 = PokerHand("2S 2H 4H 5S 4C")
print(player11.compare_with("AH AC 5H 6H 7S"))
# loss
player12 = PokerHand("TS AD 3H 4S AS")
print(player12.compare_with("AH AC 5H 6H 7S"))

# runTest("Pair wins of nothing",               "Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")
# runTest("Highest card loses",                 "Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")
# runTest("Highest card wins",                  "Win",  "4S 5H 6H TS AC", "3S 5H 6H TS AC")
# runTest("Equal cards is tie",		          "Tie",  "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")
