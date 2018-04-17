def mode(a):

    check = {}
    for i in range (0,len(a)):

        if a[i] not in check:
            check[a[i]] = 1
            
        elif a[i] in check:
            check[a[i]] += 1

    common = 0
    number = 0

    for i in range (0,len(a)):

        if check[a[i]] > number:
            number = check[a[i]]
            common = a[i]

        elif check[a[i]] == number and a[i] < common:
            common = a[i]

    return common

a = [1, 2, 3, 2, 0]

common = mode(a)
print(common)
