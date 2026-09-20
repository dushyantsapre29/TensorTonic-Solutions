import math

def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    """
    Returns the cosine embedding loss as a float.
    """
    # Write code here
    # x1 = np.asarray(x1, dtype = float)
    # x2 = np.asarray(x2, dtype = float)

    dim = len(x1)
    
    x1_norm = 0.
    x2_norm = 0.
        
    for i in range(dim):
        x1_norm += math.pow(x1[i], 2)
        x2_norm += math.pow(x2[i], 2)
    
    x1_norm = math.sqrt(x1_norm)
    x2_norm = math.sqrt(x2_norm)

    element_wise_product = [x1_i*x2_i for (x1_i,x2_i) in zip(x1,x2)]

    dot_product = 0.
    
    for i in range(dim):
        dot_product += element_wise_product[i]
    
    cosine_similarity = 0.
    
    if (x1_norm==0) or (x2_norm==0):
        cosine_similarity = 0.
    else:
        cosine_similarity = float(dot_product/(x1_norm*x2_norm))
    
    if label==1:
        return 1. - cosine_similarity
    else:
        return max(0., cosine_similarity - margin)