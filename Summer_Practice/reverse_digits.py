
def reverse(self, number: int) -> int:
    # digits_list = [int(x) for x in str(number)]
    return False

negative = False
reverse_this = -382
if reverse_this < 0:
    negative = True
    reverse_this *= -1

string_list = [x for x in str(reverse_this)]
print(string_list)
if negative:
    string_list.append('-')

print(int("".join(list(reversed(string_list)))))



