import collections
from typing import List


class Solution:
    # Time complexity:O(n)
    # Space complexity: O(n)
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parents = collections.defaultdict(list)
        doubleParentedNode = 0

        for edge in edges:
            parents[edge[1]].append(edge[0])

        for child, parent in parents.items():
            if len(parent) == 2:
                doubleParentedNode = child

        # Hybrid
        if len(parents[doubleParentedNode]) > 0:
            loopParent = None
            for parentNode in parents[doubleParentedNode]:
                # find the loop elements
                loopNodes = set()
                startingNode = parentNode

                while startingNode not in loopNodes:
                    loopNodes.add(startingNode)
                    parentList = parents[startingNode]
                    if len(parentList) > 0:
                        startingNode = parentList[0]
                    else:
                        startingNode = None

                if startingNode is not None:  # if this is the loop node, and not the non loop node
                    loopParent = startingNode

            # Find the edge from the input that has two of the nodes
            edges.reverse()
            if loopParent is not None:
                for edge in edges:
                    if edge[0] == loopParent and edge[1] == doubleParentedNode:
                        return edge

            # no loop case
            return [parents[doubleParentedNode][1], doubleParentedNode]

        # Loop with root
        startingNode = edges[0][0]
        possibleLoopNodes = set()

        while startingNode not in possibleLoopNodes:
            possibleLoopNodes.add(startingNode)
            startingNode = parents[startingNode][0]

        if startingNode is not None:
            # Find loop elements
            loopNodes = set()
            while startingNode not in loopNodes:
                loopNodes.add(startingNode)
                startingNode = parents[startingNode][0]

            # Remove last
            edges.reverse()
            for edge in edges:
                if edge[0] in loopNodes and edge[1] in loopNodes:
                    return edge
