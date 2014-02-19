import sys
import math

class OutOfRangeError(ValueError):
    pass

def is_power_of_2(n):
    """
    Returns True if n is a power of 2, False otherwise.
    """
    
    # e.g. n = 4 = b0100
    #      n - 1 = 3 = b0011
    #      n & (n - 1) = b0000
    #      not(n & (n - 1)) = True
    return not(n & (n - 1))

def predict_algorithm(n):
    """
    Predicts what number is in the nth position.
    IMPORTANT: First position is 1, not 0!
    
    See the sequence notes file for an explanation of this algorithm.
    """
    
    if n < 1:
        raise OutOfRangeError("The number must be greater than 0")
    
    if n == 1:
        return 0
    
    if is_power_of_2(n):
        return (predict_algorithm(n//2) + 1) % 3
    else:
        power = math.floor(math.log(n,2))
        return (predict_algorithm(n-2**power) + 1) % 3
    
    

    
if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    
    for test in test_cases:
        n = int(test) + 1 
        # I increment because for my algorith the 1st position is n=1
        #   and for CodeEval is n=0
        
        print(predict_algorithm(n))
    

    test_cases.close()