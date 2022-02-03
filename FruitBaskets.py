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
