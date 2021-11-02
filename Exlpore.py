import random

c1 = random.normalvariate(9, 3)
c2 = random.normalvariate(7, 5)
c3 = random.normalvariate(11, 7)

# Goes to every cafeteria for 100 days each
def explore():
    c1 = 0
    c2 = 0
    c3 = 0
    for x in range(100):
        c1 += random.normalvariate(9, 3)
    for x in range(100):
        c2 += random.normalvariate(7, 5)
    for x in range(100):
        c3 += random.normalvariate(11, 7)
    return c1 + c2 + c3





