import numpy as np
N = 50
M = 3
arr1= np.random.randint(2, size = N)
arr2= np.random.randint(2, size = N)
arr3= np.random.randint(2, size = N)
arr3[arr3==0] = -1
arr1[arr1==0] = -1
arr2[arr2==0] = -1
WeightMatrix = np.zeros((N,N))
for i in range (N):
    for j in range (N):
        if i != j:
            WeightMatrix[i][j] = (arr3[i] * arr3[j] + arr1[i] * arr1[j] + arr2[i] * arr2[j]) / M
print(WeightMatrix)

for i in range (N):
    for j in range(N):
        if WeightMatrix[i][j] != WeightMatrix[j][i]:
            print("false")

