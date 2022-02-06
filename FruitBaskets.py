# https://leetcode.com/problems/fruit-into-baskets/

def getMaxFruits(fruitArray):
    s = 0
    m = 0
    b1 = -1
    b2 = -1
    maxFruits = 0

    for i in range(len(fruitArray)):
        b1 = fruitArray[i]
        b2 = -1
        fruits = 1
        for j in range(i + 1, len(fruitArray)):
            if fruitArray[j] == b1 or fruitArray[j] == b2:
                fruits += 1
            elif b2 == -1:
                b2 = fruitArray[j]
                fruits += 1
            elif fruitArray[j] != b2 and fruitArray[j] != b1:
                break
        maxFruits = max(maxFruits, fruits)

    return maxFruits


def getMaxFruits_optimised(fruitArray):
    s = 0
    m = 0
    b1 = fruitArray[s]
    b2 = -1
    maxFruits = 1

    for i in range(1, len(fruitArray)):
        if fruitArray[i] == b1:
            # maxFruits = max(maxFruits, i - s + 1)
            if fruitArray[m] == b2:
                m = i
        elif fruitArray[i] == b2:
            # maxFruits = max(maxFruits, i - s + 1)
            if fruitArray[m] == b1:
                m = i
        elif b2 == -1:
            b2 = fruitArray[i]
            # maxFruits = max(maxFruits, i - s + 1)
            m = i
        elif fruitArray[i] != b2 and fruitArray[i] != b1:
            maxFruits = max(maxFruits, (i - 1) - s + 1)
            s = m
            m = i
            b1 = fruitArray[s]
            b2 = fruitArray[i]
            maxFruits = max(maxFruits, i - s + 1)
    return max(maxFruits, len(fruitArray) - s)
