
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1    =   len(word1)
        len2    =   len(word2)
        wordC   =   ""
        if  len1    ==  len2:
            for a   in  range(len2):
                wordC   +=  word1[a]
                wordC   +=  word2[a]
        else:
            if  len1    <   len2:
                for a   in  range(len1):
                    wordC   +=  word1[a]
                    wordC   +=  word2[a]
                wordC   +=  word2[len1::]
            if  len1    >   len2:
                for a   in  range(len2):
                    wordC   +=  word1[a]
                    wordC   +=  word2[a]
                wordC   +=  word1[len2::]
        return  wordC
#https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75