class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)

        sSorted = sorted(s)

        for char in sSorted:
            hashMap[char] +=1
        print(hashMap)


        tSorted = sorted(t)
        for char in tSorted:
            if char not in hashMap or len(s) != len(t):
                return False
        
        print(tSorted)
        
        return True