class Solution:
    def isValid(self, s: str) -> bool:
        matching_chars = {"}": "{", ")": "(", "]": "["}
        curStack = []
        for char in s:
            #opening char
            if char not in matching_chars.keys():
                curStack.append(char)
            elif curStack and curStack[-1] == matching_chars[char]:
                curStack.pop()
            #mismatched key found
            else:
                return False
        return True if not curStack else False

        #This initial version would fail if we had "{{{"; it would return true because no mismatched key, however these keys are never closed in the first place
        #     char_appearances[char] = char_appearances.get(char, 0) + 1



    #what if this? {[(]})