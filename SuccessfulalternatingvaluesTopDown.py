#!/bin/python3




#
# Complete the 'MaxGain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY V as parameter.
#

# def MaxGain(V):
# Determine the maximum payoff of the given array of coins V for the first player

# Python3 program to find out maximum
# value from a given sequence of coins

# Returns optimal value possible that
# a player can collect from an array
# of coins of size n. Note than n
# must be even

def OptStrat(V):
    vL = len(V)
    n = vL - 1
    minimum = 0
    mem = [[minimum] * vL for i in range(vL)]

    for r in range(len(mem) - 1):
        mem[r][r + 1] = max(V[r], V[r + 1])

    calls = 0

    def OptStrat(V, iPlus1, jPlus1):  # 1,4

        nonlocal minimum
        nonlocal mem
        # iplus1 is non-zero index
        # i is zero index
        i = iPlus1 - 1
        j = jPlus1 - 1
        sect = V[i:j + 1]
        if mem[i][j] != minimum:
            return mem[i][j]
        else:
            iOption = V[i] + min(OptStrat(V, iPlus1 + 2, jPlus1), OptStrat(V, iPlus1 + 1, jPlus1 - 1))
            jOption = V[j] + min(OptStrat(V, iPlus1, jPlus1 - 2), OptStrat(V, iPlus1 + 1, jPlus1 - 1))
            return max(iOption, jOption)

    cols = [[] for i in range((n + 1) // 2)]
    for layerColSet in range((n + 1) // 2):

        cols[layerColSet] = range(2 * (1 + layerColSet), vL + 1)
        if layerColSet == (n - 1) // 2:
            cols[layerColSet] = range(vL, vL + 1)

    for layer in range(1, (n + 1) // 2):
        for i in range(1, vL - 1 - 2 * layer + 1):  # rows
            j = cols[layer][i - 1]
            mem[i - 1][j - 1] = OptStrat(V, i, j)
    return mem[0][vL - 1]


