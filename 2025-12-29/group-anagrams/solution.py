class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We need to combine anagrams together, how to do? first create a hashmap using defaultdict(list)
        hashMap = defaultdict(list)
        
        for words in strs:
            sortedwords = ''.join(sorted(words))
            hashMap[sortedwords].append(words)
            
        return list(hashMap.values())