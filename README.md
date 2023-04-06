# eigenvalue_method
Similarity algorithm for (undirected, fully connected) graphs based on largest eigenvalues of the Laplacian.


**ev_method(G1,G2,threshold)**

Parameters:

*G1, G2*: graphs to compare

*threshold*: minimum of energy to be covered by the eigenvalues (default 90%). Small values are ommitted.

***returns:*** distance score (between 0 and inf).
