def minInContext(n):
    return -10000 * n + n * (n + 1)


def MaxGain(V):
    # Determine the maximum payoff of the given array of coins V for the first player
    vL = len(V)
    min = minInContext(vL / 2)

    mem = [[min] * vL for i in range(vL)]
    # for i in range(vL):

    # for j in range(vL):

    # print(f"MaxGain({i},{j},{min})")
    # mem[i].append(min)

    for r in range(len(mem) - 2):
        mem[r][r + 1] = max(V[r], V[r + 1])
        # print(type(mem[r][r+1]))
    print(mem)

    calls = 0

    def MaxGain(V, iPlus1, jPlus1) -> int:  # 1,4

        nonlocal min
        nonlocal mem
        nonlocal calls
        calls += 1
        # iplus1 is non-zero index
        # i is zero index
        i = iPlus1 - 1
        j = jPlus1 - 1
        sect = V[i:j + 1]
        print(f"MaxGain({sect},{iPlus1},{jPlus1})")
        # print(calls)
        if mem[i][j] != min:
            return mem[i][j]
        else:

            # tr_i_side = MaxGain(V,iPlus1+2,jPlus1)
            # tr_i_mid = MaxGain(V,iPlus1  + 1,jPlus1 - 1)
            # min2(tr_i_side, tr_i_mid) + i
            # tr_j_side = MaxGain(V,iPlus1,jPlus1-2)
            # tr_j_mid = MaxGain(V,iPlus1  + 1,jPlus1 - 1)
            iOption = V[i] + min(
                MaxGain(V, iPlus1 + 2, jPlus1),
                MaxGain(V, iPlus1 + 1, jPlus1 - 1)
            )
            print(iOption + "hi")

            jOption = V[j] + min(
                MaxGain(V, iPlus1, jPlus1 - 2),
                MaxGain(V, iPlus1 + 1, jPlus1 - 1)
            )
            print(jOption)

            return max(iOption, jOption)
        # 3,4
        # 2,3

        # 1,2
        # 2,3

    print("VL")
    print(vL)
    print("VL")
    # print(list(range(1,vL)))
    for i in range(1, vL + 1):  # row 1 to n
        # print(list(range(i+1,vL+1,2)))

        for j in range(i + 1, vL, 2):  # col i+1 to  n
            # print(i)
            print(i, j)
            # print(mem)
            mem[i - 1][j - 1] = MaxGain(V, i, j)
    return mem[0][vL - 2]
