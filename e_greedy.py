import random

# use of percentages is not correct
# everyday we have to randomly choose if we want the best cafeteria or if we choose randomly
def e_greedy(e):
    c1 = random.normalvariate(9, 3)
    c2 = random.normalvariate(7, 5)
    c3 = random.normalvariate(11, 7)

    if c1 > c2 and c1 > c3:
        for x in range(300 - ((e * 100) / 300)):
            c1 += random.normalvariate(9, 3)
    elif c2 > c1 and c2 > c3:
        for x in range(300 - ((e * 100) / 300)):
            c2 += random.normalvariate(7, 5)
    elif c3 > c1 and c3 > c2:
        for x in range(300 - ((e * 100) / 300)):
            c3 += random.normalvariate(11, 7)

    for x in range((e * 100) / 300):
        x = random.randint(1, 3)
        if x == 1:
            c1 += random.normalvariate(9, 3)
        if x == 2:
            c2 += random.normalvariate(7, 5)
        if x == 3:
            c3 += random.normalvariate(11, 7)

    return c1 + c2 + c3





