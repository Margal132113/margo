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

# test of symmetry
print((WeightMatrix == WeightMatrix.transpose()).all())

# test of the diagonal
diag_test = ([WeightMatrix[i][i] for i in range(WeightMatrix.shape[0])] == np.zeros((N, N))).all()
print(diag_test)


# test of the range of the weights

# could be useful later on but not sure it is necessary to define a specific function
def check_range(lower_boundary, upper_boundary, element):
    if lower_boundary <= element <= upper_boundary:
        return bool(1)
    else:
        return bool(0)


mistaken_weight = 0

for i in range(WeightMatrix.shape[0]):
    for j in range(WeightMatrix.shape[1]):
        if not (check_range(-1, 1, WeightMatrix[i][j])):
            print(WeightMatrix[i][j])
            mistaken_weight += 1

if mistaken_weight == 0:
    print(bool(1))

# print( np.random.choice([-1,1],(1,N)))
# other idea I had for the formation of pattern
# but since we don't specify the probability uses uniform distribution and we don't want that

to_change = np.random.randint(0, N, size=3)

arr3_new = arr3.copy()
print(arr3_new)


for i in to_change:
    if arr3_new[i] == -1:
        arr3_new[i] = 1
    else:
        arr3_new[i] = -1

for j in range(N):
    if arr3[j] != arr3_new[j]:
        print(arr3[j], arr3_new[j])





def update_rule(x):
    if x < 0:
        return -1
    else:
        return 1
