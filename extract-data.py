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
import pandas as pd


#lab = open("EUcountries_labels.txt","r")
#labels = lab.read().splitlines()
#print(labels) 
 



#lab = open("EUcountries_labels.txt","r")

#lab = open("EUcountries_labels.txt","r")
#labels = lab.read().splitlines()t
#print(labels) 
 




web = nx.Graph()

web_dict = defaultdict(nx.Graph)

weight_dict = defaultdict(list)

 
with open("ICIO2016_2007.csv", encoding="utf8", errors='ignore') as csv_file:
	csv_reader = csv.reader(csv_file)
#	print(line[625])in csv_reader

#	with open('new.csv', 'w') as new_file:
#		csv_writer = csv.writer(new_file, delimiter=",")
	Adj_weighted = []
	row_idx = 0
	for line in csv_reader:
		if row_idx == 0:
			row_idx += 1
			continue
		 
		elif row_idx in (list(range(47, 51)) + list(range(81, 85)) + list(range(217, 221))+list(range(285, 289))+list(range(319, 323))+list(range(353, 357))+list(range(557, 561))+list(range(829, 833))):
#			+list(range(897, 901))+list(range(999, 1003))+list(range(1135, 1139))):
#		elif row_idx in (list(range(47, 51)) + list(range(81, 85)) + list(range(217, 221))+list(range(319, 323))+list(range(557, 561))+list(range(829, 833))+list(range(897, 901))+list(range(999, 1003))+list(range(1135, 1239))):
#		elif row_idx in (list(range(47, 51)) + list(range(217, 221))+list(range(319, 323))+list(range(829, 833))+list(range(999, 1003))+list(range(1135, 1139))):
 #           
#elif row_idx in (list(range(1, 34))):
#			csv_writer.writerow(line[1: 8])
#			print(list(line[1:100]))
#			Adj_weighted.append(list(line[1:100]) + list(line[200:210]))
#			Adj_weighted.append(list(line[625:629])+list(line[1543:1547])+list(line[591:595])+list(line[1577:1581])+list(line[1713:1717])+list(line[1815:1819])+list(line[1951:1955])+list(line[1985:1989])+list(line[2053:2057])+list(line[2087:2091])+list(line[2291:2295]))
#			Adj_weighted.append(list(line[625:629])+list(line[591:595])+list(line[1713:1717])+list(line[1951:1955])+list(line[1985:1989])+list(line[2053:2057])+list(line[2087:2091])+list(line[2291:2295]))
			# Adj_weighted.append(list(line[47:51])+list(line[81:85])+list(line[217:221])+list(line[285:289])+list(line[319:323])+list(line[353:357])+list(line[557:561])+list(line[829:833])+list(line[897:901])+list(line[999:1003])+list(line[1135:1139]))
			Adj_weighted.append(list(line[47:51])+list(line[81:85])+list(line[217:221])+list(line[285:289])+list(line[319:323])+list(line[353:357])+list(line[557:561])+list(line[829:833]))
#			+list(line[897:901])+list(line[999:1003])+list(line[1135:1239])
#Adj_weighted.append(list(line[47:51])+list(line[217:221])+list(line[319:323])+list(line[829:833])+list(line[999:1003])+list(line[1135:1139]))
	
			row_idx += 1
		else:
			row_idx += 1


Adj_weighted=np.array(Adj_weighted)
np.fill_diagonal(Adj_weighted, 0)
print(Adj_weighted)
Adj_weighted = Adj_weighted.astype(np.float64)
# Adj_weighted = Adj_weighted.max() - Adj_weighted

Adj_weighted = Adj_weighted.T / (np.sum(Adj_weighted, axis=1).T+1e-16)
# Adj_weighted += 0 + 10**(-10)
# Adj_weighted = np.log(Adj_weighted)
Adj_weighted = 1 - Adj_weighted.T 
np.fill_diagonal(Adj_weighted, 1)
np.savetxt("linda3.csv", Adj_weighted, delimiter=",")



print(Adj_weighted.max())
for i in range(0, 32):
  	x = Adj_weighted
  	x = np.delete(x, i, 0)
  	x = np.delete(x, i, 1)
  	sio.savemat(f'dissim-2011-{i}.mat', {'var': x})

sio.savemat('dissim-2007-standard.mat', {'var': Adj_weighted})	