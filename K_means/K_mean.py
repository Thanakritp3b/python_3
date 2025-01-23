import random
import matplotlib.pyplot as plt
import time
import numpy as np
from math import sqrt

def gen_points(centroids, points_per_cent = 300 ,std_dev = 2.0):
    points = []
    for cx, cy in centroids:
        for _ in range(points_per_cent):
            x = random.gauss(cx, std_dev)
            y = random.gauss(cy, std_dev)
            points.append([x, y])
    return points

def euclidean_dist(p1, p2):
    return sqrt((p1[0] - p2[0]) **2 + (p1[1] - p2[1])**2 )

def find_nearest_centroid(point, centroids):
    min_dist = float('inf')
    nearest = 0
    for i,centroid in enumerate(centroids):
        dist = euclidean_dist(point, centroid)
        if dist< min_dist:
            min_dist = dist
            nearest = i
    return nearest

def cal_centroid(points , assign, k):
    new_centroids = [[0,0] for _ in range(k)]
    ct = [0] * k
    for point, cluster in zip(points,assign):
        new_centroids[cluster][0] += point[0]
        new_centroids[cluster][1] += point[1]
        ct[cluster] += 1
    
    for i in range(k):
        if ct[i] > 0:
            new_centroids[i][0] /= ct[i]
            new_centroids[i][1] /= ct[i]
    return new_centroids

def k_means(points, k, max_iter= 500):
    x_min = min(p[0] for p in points )
    x_max = max(p[0] for p in points )
    y_min = min(p[1] for p in points )
    y_max = max(p[1] for p in points )

    centroids = [[random.uniform(x_min, x_max), 
                  random.uniform(y_min, y_max)] for _ in range(k)]
    
    for _ in range(max_iter):
        assign = [find_nearest_centroid(p, centroids) for p in points]
        new_centroids = cal_centroid(points, assign, k)
        if all(euclidean_dist(old, new) < 0.0001 
               for old, new in zip(centroids, new_centroids)):
            break
        centroids = new_centroids
    
    print(f"original centroid = {centroids}")
    print(centroids)
    return assign, centroids


def K_mean_withnumpy(point_arr, k, max_iter = 500):
    centroid_cut = np.random.choice(len(point_arr), k, replace = False)
    centroids = point_arr[centroid_cut]

    for _ in range (max_iter):
        distances = np.sqrt(((point_arr[:, np.newaxis, :] - centroids) ** 2).sum(axis=2))
        assign = np.argmin(distances, axis=1)
        new_centroids = np.array([point_arr[assign == i].mean(axis=0) 
                                 for i in range(k)])
        if np.all(np.abs(centroids - new_centroids) < 0.0001):
            break
            
        centroids = new_centroids
    

    print(f"numpy centroid = {centroids}")
    return assign, centroids




def plot_cluster(points, assign, centroids, file, title):
    colors = ['r', 'g', 'b', 'y', 'c', 'm']  # Colors
    
    plt.figure(figsize=(16, 10))
    
    for point, cluster in zip(points, assign):
        color = colors[cluster % len(colors)]
        plt.scatter(point[0], point[1], c=color, alpha=0.5, s=30)
    
    for i, (cx, cy) in enumerate(centroids):
        plt.scatter(cx, cy, c='black', marker='x', s=200, linewidths=3)
    
    plt.title(title)
    plt.savefig(file)
    plt.close()

def main():
    initial_centroids = [
        [5, 5],
        [-3, -3],
        [5, -3],
        [-3, 5]
    ]
    points = gen_points(initial_centroids)
    points_arr = np.array(points)
    plt.figure(figsize = (16,10))
    for x, y in points:
        plt.scatter(x, y, c='blue', alpha=0.5, s=30)
    for x, y in initial_centroids:
        plt.scatter(x, y, c='red', marker='x', s=200, linewidths=3)
    plt.title('Initial Data Points')
    plt.savefig('initial_points.png')
    plt.close()

    k = len(initial_centroids)
    start_time = time.time()
    assignments, final_centroids = k_means(points, k)
    end_time = time.time()
    
    print(f"original Time taken: {end_time - start_time} seconds")

    plot_cluster(points, assignments, final_centroids, 'k_means_result.png','original')

    start_time = time.time()
    assignments_numpy, final_centroids_numpy = K_mean_withnumpy(points_arr, k)
    end_time = time.time()
    
    print(f"numpy Time taken: {end_time - start_time} seconds")

    plot_cluster(points, assignments_numpy, final_centroids_numpy, 'k_means_result_numpy.png','numpy')

if __name__ == "__main__":
    main()




        
        
