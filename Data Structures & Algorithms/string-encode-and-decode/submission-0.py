class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""

        for s in strs:
            final_str += str(len(s)) + "#" + s

        print(final_str)
        return final_str 


    def decode(self, s: str) -> List[str]:
        strings = []

        current_str = s
        while len(current_str) > 0:
            length = int(current_str[:current_str.index("#")])
            start = current_str.index("#") + 1
            end = start + length 
        
            strings.append(current_str[start:end])
            current_str = current_str[end:]

        return strings
