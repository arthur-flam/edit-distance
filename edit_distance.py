import numpy as np

def edit_distance(s, t):
    """
    Computes the edit distance between two strings.
    Additions, deletions and edits all have the same cost, 1.
    """
    distances = np.zeros((len(s) + 1, len(t) + 1))
    for i_s in range(len(s) + 1):
        for i_t in range(len(t) + 1):            
            d = np.inf
            if i_t == 0 and i_s == 0:
                continue
            if i_t > 0:
                d = min(d, distances[i_s, i_t - 1] + 1)
            if i_s > 0:
                d = min(d, distances[i_s - 1, i_t] + 1)
                if i_t > 0:
                    d = min(d, distances[i_s - 1, i_t - 1] + int(s[i_s-1]!=t[i_t-1]) )
            distances[i_s, i_t] = d
    return distances[len(s)-1, len(t)-1]
# djikstra
# dynamic programming



