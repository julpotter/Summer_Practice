L = [2, 3, 2, 1, 0, 1, 3, 3, 2, 0, 1, 1, 2]
P = 2

def initialize_list(L, P):
    last_index = 0
    num_sums = len(L) - 1 - P  # Times multiplied
    sums = [[]]

    for i in range(num_sums-1):
        print(sums)
        sums.append([])

    for i in range(len(sums)):
        sums[i].append(L[i])
        last_index = i
        print(last_index)

    for i in L[last_index-1:]:
        sums[-1].append(i)

    return sums



def find_max(sums, max_solution):
    shift = 0
    visited_first = False
    mult = 1

    for i in sums:
        mult *= sum(i)
    if mult > max_solution:
        max_solution = mult

    for item in reversed(sums):
        if not visited_first:
            shift = item[0]
            visited_first = True
            continue
        item.append(shift)
        shift = item[0]
        del item[0]

    if len(sums[-1]) <= 1:
        return max_solution
    else:
        find_max(sums, max_solution)


def max_add_mult(L, P):
    shift = 0
    visited_first = False
    mult = 1
    sums = initialize_list(L, P)
    find_max(sums, 0)

    #
    # num_sums = len(L) - 1 - P
    # if times_multiplied < num_sums:
    #     times_multiplied += 1
    # else:
    #     return








print(max_add_mult(L, 8))