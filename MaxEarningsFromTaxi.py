# https://leetcode.com/problems/maximum-earnings-from-taxi/
from typing import List


def getMoney(ride: List[int]):
    return ride[1] - ride[0] + ride[2]


def getMaxEarningsFromTaxiRec(n: int,
                              currentN: int,
                              rides: List[List[int]],
                              currentRideIndex: int,
                              maxSoFar: int
                              ):
    # Stop if all rides are selected and count the money
    if currentRideIndex >= len(rides):
        return maxSoFar

    # Skip if the ride is behind the current position of the passenger. Although, this can't happen if skipped in currentN
    if currentN > rides[currentRideIndex][0]:
        return getMaxEarningsFromTaxiRec(n, currentN, rides, currentRideIndex + 1, maxSoFar)

    # Pick or skip the ride
    return max(getMaxEarningsFromTaxiRec(n, rides[currentRideIndex][1], rides, currentRideIndex + 1, maxSoFar + getMoney(rides[currentRideIndex])),  # pick
               getMaxEarningsFromTaxiRec(n, currentN, rides, currentRideIndex + 1, maxSoFar))  # skip


def getMaxEarningsFromTaxi(n: int, rides: List[List[int]]):
    rides.sort(key=lambda ride: ride[0])

    return getMaxEarningsFromTaxiRec(n, 0, rides, 0, 0)
