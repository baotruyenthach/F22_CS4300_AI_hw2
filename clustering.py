import matplotlib.pyplot as plt 
import numpy as np 

np.random.seed(10)

# TODO: Enter your membership assignments here 
cluster_1 = np.array([[0,0], [1,1], [2,2]]) 
cluster_2 = np.array([[3,3], [4,4], [4,4]]) 

# TODO: Enter your cluster centers here
center_1 = [-1,-1]
center_2 = [5,5]


plt.plot(cluster_1[:,0], cluster_1[:,1], "ro") 
plt.plot(cluster_2[:,0], cluster_2[:,1], "go") 
plt.plot(center_1[0], center_1[1], "r*", markersize=20) 
plt.plot(center_2[0], center_2[1], "g*", markersize=20) 

plt.title("k-means clustering")
plt.xlabel("x")
plt.ylabel("y")
plt.show()