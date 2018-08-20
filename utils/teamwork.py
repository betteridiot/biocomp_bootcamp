from random import shuffle, sample


def paired_programming(roster, k):
    """Creates randomly assigned groups from a class roster without replacement
    
    If the roster is not divisible by k, last item will return the remainder of roster
    as a deficient group.
    
    Args:
        roster (iterable): any iterable containing the the class roster
        k (int): the size of the groups
    
    Yields:
        pair (tuple): a k-item tuple containing the randomly assigned groups
    """
    changing_roster = set(roster)
    while True:
        if k >= len(changing_roster):
            yield tuple(changing_roster)
            break
        pair = sample(changing_roster, k)
        for person in pair:
            changing_roster = changing_roster.difference(set((person,)))
        yield tuple(pair)
