# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

recursions = 0
memo = {}

def getLengthLongestCommonSubsequenceRec(s1, s2, s1i, s2i):
    global recursions
    recursions += 1
    global memo
    maxSavedValue = memo.get((s1i, s2i))

    if maxSavedValue is not None:
        return maxSavedValue

    if s1i >= len(s1) or s2i >= len(s2):
        memo[(s1i, s2i)] = 0
        return 0

    if s1[s1i] == s2[s2i]:
        value = getLengthLongestCommonSubsequenceRec(s1, s2, s1i + 1, s2i + 1) + 1
        memo[(s1i, s2i)] = value
        return value

    valueWithIncrementI = getLengthLongestCommonSubsequenceRec(s1, s2, s1i + 1, s2i)
    memo[(s1i, s2i)] = valueWithIncrementI
    valueWithIncrementJ = getLengthLongestCommonSubsequenceRec(s1, s2, s1i, s2i + 1)
    memo[(s1i, s2i)] = valueWithIncrementJ
    return max(valueWithIncrementI,
               valueWithIncrementJ)

def getLengthLongestCommonSubsequenceRecursiveOptimised(s1, s2):
    global recursions
    if s1 == "" or s2 == "":
        return 0

    rec = getLengthLongestCommonSubsequenceRec(s1, s2, 0, 0)
    print(f"recursion = {recursions}")
    return rec
