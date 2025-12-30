class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        sentence = []
        for words in strs:
            
            word = words +'#'
            # print(word)
            sentence.append(word)
            # print(sentence)

        final = ''.join(sentence)
        print(final)
        return final

    def decode(self, s: str) -> List[str]:
        print(s)

        rejoin = [s]
        print(rejoin)
        tempword =''
        checkWord = ''
        res = []

        for char in s:
            checkWord += char
            print(checkWord)
            if char != "#" or checkWord == "%##%":
                tempword += char
                print(tempword)

            else:
                res.append(tempword)
                tempword = ''
                print(res)
        return res

