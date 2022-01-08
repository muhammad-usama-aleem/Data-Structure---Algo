'''
find first non-recursive integer from the given array

solution:
used 2 arrays as 2 filter pass
first array stores all the values that come as input just like set
second array stores all the non-recursive element

'''


def finding(arr):
    first = []
    second = []
    for val in arr:
        # print(val)
        if val in first:
            if val in second:
                second.remove(val)
        if val not in first:
            first.append(val)
            second.append(val)
    print("first", first)
    print("second", second)
    return second[0]


# finding([1, 1, 1, 2, 2, 2, 3, 3, 4, 4])
finding([1, 5, 4, 7, 7])
