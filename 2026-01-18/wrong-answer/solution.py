class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)

        for char in s:
            hashMap[char] +=1
        print(hashMap)

        wordMap = dict(sorted(hashMap.items()))
        print(wordMap)


        for char in t:
            if char not in wordMap:
                print(char)
                return False
        return True