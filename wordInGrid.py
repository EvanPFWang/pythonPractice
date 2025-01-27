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
        return  delta
    return False





def wordInGrid(matrix,word):
    wordLen = len(word)

    n = len(matrix)
    m = len(matrix[0])
