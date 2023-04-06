import networkx as nx
import numpy as np

def k(spectrum, threshold = 0.9):
    total = sum(abs(spectrum))
    if total == 0.0:
        return len(spectrum)
    i_total = 0.0
    for i in range(len(spectrum)):
        i_total += spectrum[i]
        if i_total / total >= threshold:
            return i + 1
    return len(spectrum)

def ev_method(G1,G2,threshold = 0.9):
    l1 = np.array(sorted(nx.spectrum.laplacian_spectrum(G1)))
    l2 = np.array(sorted(nx.spectrum.laplacian_spectrum(G2)))
    k1 = k(l1)
    k2 = k(l2)
    k = min(k1, k2,threshold)
    distance = sum((l1[:k] - l2[:k])**2)
    return distance
