class   Solution:
    def currentSearch(self,matrix,word,x,y,wordIndexOn):
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
            deltaBool   =   (self.currentSearch(matrix,word,x-1,y,wordIndexOn+1) or
                        self.currentSearch(matrix,word,x,y-1,wordIndexOn+1) or
                        self.currentSearch(matrix,word,x,y+1,wordIndexOn+1) or
                        self.currentSearch(matrix,word,x+1,y,wordIndexOn+1))
            matrix[x][y] = temp
            return  deltaBool
        return False




    def gen(self,n):
        i = 0
        while i < n:
            yield i
            i += 1


    def exist(self, matrix: List[List[str]], word: str) -> bool:
        wordLen = len(word)
        n = len(matrix)
        m = len(matrix[0])

        if wordLen > n * m:
            return False

        for i in self.gen(n):
            for j in self.gen(m):
                if matrix[i][j] == word[0]:
                    if self.currentSearch(matrix, word, i, j, 0):
                        return True
        return False

