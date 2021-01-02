
def strStr(haystack: str, needle: str) -> int:
    N = len(needle)
    if not needle:
        return 0
    for i in range(len(haystack)):
        end_point = i + N
        substring = haystack[i:end_point]
        if substring == needle:
            return i

    return -1





haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))