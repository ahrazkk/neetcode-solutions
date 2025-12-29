class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}


        for integer in nums:
            if integer in hashMap:
                 hashMap[integer] += 1
            else:
                hashMap[integer] = 1
            
        # print(hashMap)
        # sortedMap = sorted(hashMap, reverse = True) this worked but only sorts based of key not count, need lambda
        # function to change the focus in reverse key = lambda item:item[1] 1 for the second nummber, but also need
        # to add hashMap.items otherwise it does not see the second value in the first place
        sortedMap = sorted(hashMap.items(), key = lambda item:item[1], reverse = True)
        # print(sortedMap)
        
        # now we need it so that instead of returning the tuples of k, we just return the number key not frequancy
        print(sortedMap)

        # We got to the part of having it in the form of: [(3, 3), (2, 2), (1, 1)], but thats not good, we 
        # need to have it only return the k amount and also return only key in an array

        Final_list = [] # initialize an array
        for items in sortedMap[:k]: #itterate over values that in sorted map up to k amount, we already did the ordering so its fine
            print(items)
            number = items[0] # make number hold the first key and then add that key to the array
            Final_list.append(number)
            print(Final_list)
            

        return Final_list

