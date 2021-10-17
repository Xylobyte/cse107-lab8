def element_of(element, l):
    """
    returns if an element is within the given list. Calls itself again 
    if a nested list is found

    element: the element to search for.
    l: the list to check for the element.
    """
    for e in l:
        if e == element:
            return True
        elif type(e) == list:
            result = element_of(element, e)
            if result:
                return True
    return False


def filter_by_depth(depth, l):
    """
    returns the list with all given lists at a given depth.

    depth: the depth to check the list for.
    l: the list to check.
    """
    r = []
    if depth == 0:
        return r
    for e in l:
        if type(e) == list:
            if depth == 1:
                del e
            else:
                r.append(filter_by_depth(depth - 1, e))
        else:
            r.append(e)
    return r


def main():
    pass


if __name__ == "__main__":
    main()
