import random
from operator import itemgetter

ERROR_EPS = 1e-6
MAX_ITERATIONS = 10000


def k_means(in_points, in_clusters_number):
    if len(in_points) < in_clusters_number:
        return None
    centroid_points = random.sample(in_points, in_clusters_number)
    centroids = [(index, elem)
                 for index, elem in enumerate(centroid_points)]

    error = 999999
    counter = 0
    while ERROR_EPS < abs(error) and counter < MAX_ITERATIONS:
        counter += 1
        error = 0
        clusters = {index: set([]) for index in xrange(len(centroids))}
        for point in in_points:
            distances = [(index, abs(point - centroid_coord))
                         for index, centroid_coord in centroids]
            closest_distance = min(distances, key=itemgetter(1))
            error += closest_distance[1]
            clusters[closest_distance[0]].add(point)
        centroids = [(index, sum(points) / float(len(points)))
                     for index, points in clusters.iteritems()]
    return clusters


if __name__ == '__main__':
    print k_means([0, 1, 2, 3, 9, 15, 18, 99, 80, 81], 3)
