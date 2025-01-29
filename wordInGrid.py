def currentSearch(matrix,word,x,y,wordIndexOn):
    n   = len(matrix)
    m   = len(matrix[0])
    wordLen = len(word)
    if wordIndexOn == wordLen:
        return True
    if  x<0 or x>=n or y<0 or y>=m:
        return False
    cursor  =   matrix[x][y]
    if cursor == word[wordIndexOn]:

        temp    = matrix[x][y]
        matrix[x][y] = "~"
        delta   =   (currentSearch(matrix,word,x-1,y,wordIndexOn+1),
                     currentSearch(matrix,word,x,y-1,wordIndexOn+1),
                     currentSearch(matrix,word,x,y+1,wordIndexOn+1),
                     currentSearch(matrix,word,x+1,y,wordIndexOn+1))
        matrix[x][y] = temp
        return  deltaBool
    return False




def gen(n):
    i = 0
    while i < n:
        yield i
        i += 1



        # If first letter matches, then recur and check
        if mat[i][j] == word[0]:
            if findMatch(mat, word, i, j, 0):
                return True


def wordInGrid(matrix,word):
    wordLen = len(word)

    n = len(matrix)
    m = len(matrix[0])

    if wordLen  <   n*m:
        return False
    for i in gen(n):
        for j in gen(m):
            if  matrix[i][j] == word[0]:
                if findMatch(matrix, word, i, j, 0):
                    return True
    return False

