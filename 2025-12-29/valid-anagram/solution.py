class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HashMap = {}


# Solution was harder then expected, first used HashSet, failed when I got to bbcc,ccbc, since the set contained
# both letters, Learned about HashMaps [A:2], this tracks the amount of times a char appears, 



        for characters in s:
            if characters in HashMap:
                HashMap[characters] = HashMap[characters] + 1
            else:
                HashMap[characters] = 1
        
        #print(HashMap)

        for character in t:
            if character not in HashMap or len(s) != len(t):
                return False
            else:
                HashMap[character] =  HashMap[character] - 1
                if HashMap[character] <0 :
                    print(HashMap)
                    return False
            
        
        return True