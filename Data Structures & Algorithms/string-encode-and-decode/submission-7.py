class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in range(len(strs)):
            result = result + str(len(strs[word])) + "#" + strs[word] 
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word = s[j+1:j + length+1]
            result.append(word)
            i = j + length + 1
        return result
