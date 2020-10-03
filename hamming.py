def distance(strand_a, strand_b):
    hamming = 0
    if len(strand_a) == len(strand_b):
        for x, y in zip(strand_a, strand_b):
            if x != y:
                hamming = hamming + 1
        return hamming
