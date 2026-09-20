import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    dim = len(x)

    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    return float(np.dot(x,y))
    
    # This works, doesn't use numpy
    # prod = [xi*yi for (xi,yi) in zip(x,y)]
    # sum = 0
    
    # for i in range(len(prod)):
    #     sum += prod[i]
        
    # return float(sum)