k = 10
q = 10
j = 10
a = 1

def score_of_hand(hand):
    score = sum(hand)
    if a in hand:
        if score<=11:
            score += 10
    return score


if __name__ == "__main__":
    assert(score_of_hand([j,6])==16)
    assert(score_of_hand([8,6])==14)
    assert(score_of_hand([a,10])==21)
    assert(score_of_hand([a,8,4])==13)
    assert(score_of_hand([a,a,a,a,2,2,2,2,3,3,3])==21)


