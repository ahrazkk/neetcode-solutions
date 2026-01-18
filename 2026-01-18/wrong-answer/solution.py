class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)
        tMap = defaultdict(int)

        for char in s:
            hashMap[char] +=1
        # print(hashMap)

        wordMap = dict(sorted(hashMap.items()))
        print(wordMap)



        for char in t:
            tMap[char] +=1 
            if char not in wordMap or len(s) != len(t):
                return False
        
        return True