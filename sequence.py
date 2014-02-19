def make_sequence(iterations, seed="0"):
    """
    Constructs the exercise's sequence as a string.
    Used for testing only.
    """
    
    sequence = seed
    for i in range(0, iterations):
        seed = sequence
        for c in seed:
            new = (int(c) + 1) % 3 
            sequence += str(new)
        
    return sequence