def faculty(a):

    """ Calculates the faculty of the number a """

    if a > 0:
        a = a * faculty(a-1)
        return a
    elif a == 0:
        return 1
    else:
        return -1
def main():

    """ Check the value of a few numbers """
    
    assert faculty(3) == 6
    assert faculty(2) == 2
    assert faculty(1) == 1
    assert faculty(0) == 1
    assert faculty(-1) == -1
    assert faculty(-2) == -1

main()
