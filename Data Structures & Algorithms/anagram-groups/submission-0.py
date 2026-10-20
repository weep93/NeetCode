class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_container = {}
        for word in strs:
            sorted_key = "".join(sorted(word)) #key value after joined


            word_container.setdefault(sorted_key, []).append(word)


        ## formating output 
        return(list(word_container.values()))