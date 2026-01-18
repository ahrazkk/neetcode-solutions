class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)

        for char in s:
            hashMap[char] +=1
        # print(hashMap)

        wordMap = dict(sorted(hashMap.items()))
        # print(wordMap)

        sSorted = sorted(s)
        print(sSorted)
        tSorted = sorted(t)
        print(tSorted)

        for char in t:
            if char not in wordMap or len(s) != len(t)  :
                # print(char)
                return False
        return True