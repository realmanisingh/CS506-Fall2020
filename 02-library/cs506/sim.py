def euclidean_dist(x, y):
    """
    Calculates the Euclidean distance between two data points
    param x: A list of integers
    param y: A list of integers
    return: The Euclidean distance between the two data points, integer
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    
    i = 0
    residual = 0
    while i < len(x):
        residual += abs(x[i] - y[i])**2
        i += 1
    return residual**(1/2)

def manhattan_dist(x, y):
    """
    Calculates the Manhattan distance between two data points
    param x: A list of integers
    param y: A list of integers
    return: The Manhattan distance between the two data points, integer
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    i = 0
    residual = 0
    while i < len(x):
        residual += abs(x[i] - y[i])
        i += 1
    return residual

def jaccard_dist(x, y):
    """
    Calculates the Jaccard distance between two data points
    param x: A list of integers
    param y: A list of integers
    return: The Jaccard distance between the two data points, integer
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    
    i = 0
    intersection = 0
    union = 0
    while i < len(x):
        if x[i] == y[i]:
            intersection += 1
        else:
            union += 1
        i += 1
        
    union += intersection
        
    jaccard_similarity = 0
    try:
        jaccard_similarity = intersection / union
    except ZeroDivisionError as e:
        e = "Lengths of input vectors must not be equal to zero"
    
    return 1 - jaccard_similarity

def cosine_sim(x, y):
    """
    Calculates the Manhattan distance between two data points
    param x: A list of integers
    param y: A list of integers
    return: The Manhattan distance between the two data points, integer
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    
    dot_product = sum(i[0] * i[1] for i in zip(x,y))
    magnitude_x = sum(i**2 for i in x)**(1/2)
    magnitude_y = sum(i**2 for i in y)**(1/2)
    
    cosine_similarity = 0
    
    try:
        cosine_similarity = dot_product / (magnitude_x * magnitude_y)
    except ZeroDivisionError as e:
        e = "Lengths of input vectors must not be equal to zero"
    
    return cosine_similarity


