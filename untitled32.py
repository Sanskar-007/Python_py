import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage, dendrogram

df=pd.read_csv("D:/ML/Datasets/nutrient.csv", index_col=0)

scaler = StandardScaler().set_output(transform='pandas')
df_scaled = scaler.fit_transform(df)
link = "single"
mergings = linkage(df_scaled,method=link)
dendrogram(mergings,
           labels=list(df_scaled.index))
plt.title(link+" linkage")
plt.show()


clust = KMeans(n_clusters=2,random_state=24)
clust.fit(df_scaled)

print(clust.labels_)
print(clust.inertia_)

################

Ks = [2,3,4,5,6,7,8,9,10]
scores = []
for i in Ks:
    clust = KMeans(n_clusters=i, random_state=24)
    clust.fit(df_scaled)
    scores.append(clust.inertia_)

plt.scatter(Ks, scores, c='r')
plt.plot(Ks,scores)
plt.title("Scree Plot")
plt.xlabel("cluster")
plt.ylabel("WSS")
plt.show()
