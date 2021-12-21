import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt
import scipy as sp 
from ripser import ripser
from persim import plot_diagrams
import csv
import math 
import os
import codecs
import scipy.io as sio
from collections import defaultdict
import numpy


#-----------------------------------------------------------------Katz Centrality
# G = nx.DiGraph()

# G.add_edges_from([('F', 'A'),('B','F'),('C','F'),('D','F'),('E','F')], weight=1)
# phi = (1 + math.sqrt(5)) / 2.0  # largest eigenvalue of adj matrix
# centrality = nx.katz_centrality_numpy(G, 1 / phi)
# for n, c in sorted(centrality.items()):
#     print(f"{n} {c:.2f}")





#-----------------------------------------------------------------Pagerank Centrality

# G = nx.DiGraph()

# G.add_edges_from([('F', 'A'),('B','F'),('C','F'),('D','F'),('E','F')], weight=1)
# pr = nx.pagerank_numpy(G, alpha=0.9)

# for n, c in sorted(pr.items()):
#     print(f"{n} {c:.2f}")




#-----------------------------------------------------------------Hub and Authority Centrality

# G = nx.DiGraph()

# G.add_edges_from([('F', 'A'),('B','F'),('C','F'),('D','F'),('E','F')], weight=1)
# h, a = nx.hits(G)

# for n, c in sorted(h.items()):
#     print(f"{n} {c:.2f}")

# for n, c in sorted(a.items()):
#     print(f"{n} {c:.2f}")


#-----------------------------------------------------------------matrix try
# import numpy as np 
# import networkx as nx 
# import matplotlib.pyplot as plt
# import scipy as sp 
# from ripser import ripser
# from persim import plot_diagrams
# import csv
# import math 
# import os
# import codecs
# import scipy.io as sio
# from collections import defaultdict
# import pandas as pd


 
# web = nx.Graph()

# web_dict = defaultdict(nx.Graph)

# weight_dict = defaultdict(list)

 
# with open("ICIO2016_2011.csv", encoding="utf8", errors='ignore') as csv_file:
# 	csv_reader = csv.reader(csv_file)
# 	Adj_weighted = []
# 	row_idx = 0
# 	for line in csv_reader:
# 		if row_idx == 0:
# 			row_idx += 1
# 			continue
# 		elif row_idx in (list(range(625, 629)) + list(range(591, 595)) + list(range(1713, 1717))+list(range(1951, 1955))+list(range(1985, 1989))+list(range(2053, 2057))+list(range(2087, 2091))+list(range(2325, 2329))):
# 			Adj_weighted.append([float(w) for w in list(line[625:629])+list(line[591:595])+list(line[1713:1717])+list(line[1951:1955])+list(line[1985:1989])+list(line[2053:2057])+list(line[2087:2091])+list(line[2325:2329])])
# 			row_idx += 1
# 		else:
# 			row_idx += 1


# Adj_weighted=np.array(Adj_weighted)
# np.fill_diagonal(Adj_weighted, 0)

A = np.array([[0, 1.0, 1, 2, 3, 4],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 6],
	[0, 0, 0, 0, 0, 0]])

A = A.transpose()

# A = np.array([[0.4, 0.0, 0.0, 0.0, 0, 0],
# 	[0.0, 0.0, 0.0, 0.0, 0, 2],
# 	[0.0, 0.0, 0.0, 0.0, 0, 3],
# 	[0.0, 0.0, 0.8, 0.0, 0, 4],
# 	[0.0, 0.0, 0.0, 0.0, 0, 5],
# 	[6.0, 0.0, 0.0, 0.0, 0, 0]])
# print(Adj_weighted)

print(A)


G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.DiGraph)
print(G)


pr = nx.pagerank_numpy(G, alpha=0.9)

for n, c in sorted(pr.items()):
    print(f"{n} {c:.2f}")



# h, a = nx.hits(G)

# for n, c in sorted(h.items()):
#     print(f"{n} {c:.2f}")

# for n, c in sorted(a.items()):
#     print(f"{n} {c:.2f}")
