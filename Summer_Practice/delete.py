
def print_nothing(str):
    if 2147483647 == 2**31 - 1:
        print("True")
    else:
        print("False")

    return ""

print(print_nothing(""))