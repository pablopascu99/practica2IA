import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cardsNuevo.csv",sep = ',')
newdf = df[["NUM_OP", "IMPORTE"]].dropna()

kmeans = KMeans(n_clusters = 4, random_state = 0).fit(newdf)
kmeans.labels_

np.unique(kmeans.labels_, return_counts = True)

plt.scatter(newdf["NUM_OP"], newdf["IMPORTE"], c= kmeans.labels_)
plt.show()