# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

longestString = ""

def getLongestCommonSubsequenceRec(s1, s2, s1i, s2i, longestSoFar):
    global longestString

    if s1i == len(s1) or s2i == len(s2):
        if len(longestSoFar) > len(longestString):
            longestString = longestSoFar
        return
    if s1[s1i] == s2[s2i]:
        longestSoFar += s2[s2i]
        getLongestCommonSubsequenceRec(s1, s2, s1i + 1, s2i + 1, longestSoFar)
    else:
        getLongestCommonSubsequenceRec(s1, s2, s1i + 1, s2i, longestSoFar)
        getLongestCommonSubsequenceRec(s1, s2, s1i, s2i + 1, longestSoFar)


def getLongestCommonSubsequenceRecursiveStart(s1, s2):
    if s1 == "" or s2 == "":
        return ""

    getLongestCommonSubsequenceRec(s1, s2, 0, 0, "")
    return longestString

if __name__ == '__main__':
    print(getLongestCommonSubsequenceRecursiveStart("ahcead", "acaed"))