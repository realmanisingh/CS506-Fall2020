from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    point_sum = [0 for x in range(len(points[0]))]
    
    for i in range(len(points)):
        for j in range(len(point_sum)):
            point_sum[j] += points[i][j]
    for i in range(len(point_sum)):
        point_sum[i] /= len(points)
    return point_sum


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    assignments_set = set(assignments)
    assignments_unique = list(assignments_set)
        
    centers = []
    for cluster_id in assignments_unique:
        points_in_clust = []
        for idx, point in enumerate(dataset):
            if cluster_id == assignments[idx]:
                points_in_clust.append(point)
        centers.append(point_avg(points_in_clust))
        
    return centers

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    if len(a) == 0 or len(b) == 0:
        raise ValueError("lengths must not be zero")
    
    if len(a) != len(b):
        raise ValueError("lengths must be equal")
    
    i = 0
    residual = 0
    while i < len(a):
        residual += abs(a[i] - b[i])**2
        i += 1
    return residual**(1/2)

def distance_squared(a, b):
    
    return distance(a, b)**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    random_points = random.sample(dataset, k)
    
    return random_points

def cost_function(clustering):
    cost = 0
    
    for key in clustering:
        mean = point_avg(clustering[key])
        for point in clustering[key]:
            cost += distance_squared(point, mean)
    
    return cost
        

def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    initial_center = generate_k(dataset, 1)
    distances = []
    
    for point in dataset:
        distances.append(distance_squared(point, initial_center[0]))
        
    probs = [i / sum(distances) for i in distances]
    data_idices = [i for i in range(len(dataset))]
    centers = []
    
    for i in range(k):
        center_idx = random.choices(population=data_idices, weights=probs, k=1)
        centers.append(dataset[center_idx[0]])
        probs[center_idx[0]] = 0
        
    return centers

def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
