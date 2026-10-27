class Solution:

    def encode(self, strs: List[str]) -> str:
        message = ""
        for s in strs:
            message += f"{len(s)}#{s}"
        return message

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            delim = s.find('#', i)
            length = int(s[i:delim])
            decoded_strs.append(s[delim + 1 : delim + 1 + length])
            i = delim + 1 + length
        return decoded_strs