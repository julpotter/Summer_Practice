from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    word = ""
    if strs == [""]:
        return ""
    for character in strs[0]:
        if character == "":
            return ""
        # print(word)
        first_letter = True
        for element in strs:
            N = len(word)
            if word != element[0:N]:
                return word[:-1]
            else:
                if first_letter:
                    word += character
                    first_letter = False
                continue
    return word


flower = ["flower", "flow", "float"]
print(longestCommonPrefix(flower))
