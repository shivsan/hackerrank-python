# https://leetcode.com/problems/maximum-earnings-from-taxi/
from typing import List


def getMoney(ride: List[int]):
    return ride[1] - ride[0] + ride[2]


def getMaxEarningsFromTaxiRec(n: int,
                              currentN: int,
                              rides: List[List[int]],
                              currentRideIndex: int,
                              memo: dict
                              ):
    # Stop if all rides are selected
    if currentRideIndex >= len(rides):
        memo[currentN] = 0
        return 0

    if currentN in memo:
        return memo[currentN]

    # Skip if the ride is behind the current position of the passenger. Although, this can't happen if skipped in currentN
    if currentN > rides[currentRideIndex][0]:
        rec = getMaxEarningsFromTaxiRec(n, currentN, rides, currentRideIndex + 1, memo)
        memo[currentN] = max(memo[currentN], rec)
        return rec

    # Pick or skip the ride
    result = max(getMaxEarningsFromTaxiRec(n, rides[currentRideIndex][1], rides, currentRideIndex + 1, memo) + getMoney(
        rides[currentRideIndex]),  # pick
                 getMaxEarningsFromTaxiRec(n, currentN, rides, currentRideIndex + 1, memo))  # skip

    memo[currentN] = result
    return result


def getMaxEarningsFromTaxi(n: int, rides: List[List[int]]):
    rides.sort(key=lambda ride: ride[0])
    memo = {}

    getMaxEarningsFromTaxiRec(n, 0, rides, 0, memo)
    return memo[0]


# Optimised - bottom up

def getMaxEarningsFromTaxiOptimisedRec(n: int,
                                       currentN: int,
                                       rides: List[List[int]],
                                       currentRideIndex: int):
    return 0


def getMaxEarningsFromTaxiOptimised(n: int, rides: List[List[int]]):
    rides.sort(key=lambda ride: ride[0])

    return getMaxEarningsFromTaxiOptimisedRec(n, 0, rides, 0)
