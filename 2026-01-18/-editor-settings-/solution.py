class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)
        tMap = defaultdict(int)

        sSorted = sorted(s)

        for char in sSorted:
            hashMap[char] +=1
        print(hashMap)


        tSorted = sorted(t)
        for char in tSorted:
            tMap[char] += 1 
            if char not in hashMap or len(s) != len(t):
                return False
        if tMap != hashMap:
            return False
        
        
        return True