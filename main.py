import numpy as np

Number_of_neurons = 50
Number_of_patterns = 3

memorized_patterns = np.random.randint(2, size=(Number_of_patterns, Number_of_neurons))
memorized_patterns[memorized_patterns == 0] = -1

pattern1 = memorized_patterns[0, ]
pattern2 = memorized_patterns[1, ]
pattern3 = memorized_patterns[2, ]

WeightMatrix = np.zeros((Number_of_neurons, Number_of_neurons))
for i in range(Number_of_neurons):
    for j in range(Number_of_neurons):
        if i != j:
            WeightMatrix[i][j] = (pattern3[i] * pattern3[j] + pattern1[i] * pattern1[j] + pattern2[i] * pattern2[j]) / Number_of_patterns
print("Weight matrix created with the patterns and the hebbian rule \n", WeightMatrix)

# test of symmetry
print("Is the matrix symmetric ? ", (WeightMatrix == WeightMatrix.transpose()).all())

# test of the diagonal
diag_test = ([WeightMatrix[i][i] for i in range(WeightMatrix.shape[0])] == np.zeros((Number_of_neurons, Number_of_neurons))).all()
print("Are the elements of the diagonal all zeros ? ", diag_test)
#------------------------------------------------------------------------------------
# CODE DE MARGOT 07.11 : DEBUT
#------------------------------------------------------------------------------------
#definition of a function that generate the patterns to memorize

def generate_patterns(num_patterns, pattern_size) :
array = np.random.randint(2, size=(num_patterns, pattern_size))
array[array == 0] = -1
    return array
# definition of a function that perturb a given pattern
def perturb_pattern(pattern, num_perturb) :
    noise = np.random.uniform(0.0, 1.0, num_perturb)
    perturbed_pattern = pattern + num_perturb
    return perturbed_pattern

# definition of a function that match a pattern with the corresponding memorized one

def pattern_match(memorized_patterns, pattern) :
    if memorized_patterns != pattern :
    else :
        for i in range (memorized_patterns.shape[1])
            if memorized_patterns[i] == pattern
                return i
# definition of a function that returns the weight matrix by applying the hebbian learning rule
def hebbian_weights(patterns) :
WeightMatrix = np.zeros((patterns.shape[0], patterns.shape[0]))
pattern_nb = patterns.shape[1]
for i in range(patterns.shape[0]):
    for j in range(patterns.shape[0]):
        if i != j:
            for nb in range (pattern_nb) :
                 WeightMatrix[i][j] = (pattern[nb][i] * pattern[nb][j] + pattern[nb+1][i] * pattern[nb+1][j]) / pattern_nb
    print("Weight matrix created with the patterns and the hebbian rule \n", WeightMatrix)


# definition of a function that apply the update rule to a state pattern
def update(state, weights) :
    newmatrix = np.dot(weights , state)
    newstate = np.zeros_like(state)
    for index in range (newmatrix.shape[0]) :
        newstate[i] = binary_rule(newmatrix[i])
    return new_state

# definition of a function that apply the asynchronous update rule to a state pattern

def update_async(state, weights) :
    i = np.random.uniform(0, state.shape[0])
    weight_vector = weights[i]
    return numpy.inner(weight_vector , state)

# definition of a function that run the dynamical system from an initial state
#            until convergence or until a maximum number of steps is reached

def dynamics(state, weights, max_iter) :
    T = 0
    intermediate_state = []
    pattern_t = np.zeros_like(state)
    # pattern_t_1 = update_async(state, weights)
while (pattern_t != state).any() and T < max_iter :
    pattern_t_1 = update_async(state, weights)
    pattern_t = pattern_t_1.copy()
    intermediate_state.append(pattern_t)
    T+=1

return (intermediate_state)

# definition of a function that run the dynamical system from an initial state
#            until a maximum number of steps is reached.



#------------------------------------------------------------------------------
#  CODE DE MARGOT 07.11 : FIN
# ---------------------------------------------------------------------------------------



# definition of a function that checks if the element is within the range

def check_range(lower_boundary=-1, upper_boundary=1, element=0):
    if lower_boundary <= element <= upper_boundary:
        return bool(1)
    else:

        return bool(0)

# test of the range of the weights


mistaken_weight = 0

for i in range(WeightMatrix.shape[0]):
    for j in range(WeightMatrix.shape[1]):
        if not(check_range(-1, 1, WeightMatrix[i][j])):
            print(WeightMatrix[i][j])
            mistaken_weight += 1


if mistaken_weight == 0:
    print("All weights are within the range [-1,1]")

# print( np.random.choice([-1,1],(1,N)))
# other idea I had for the formation of pattern
# but since we don't specify the probability uses uniform distribution and we don't want that

# Creation of a new pattern from one of the pattern memorised

Number_values_to_change = 40
# Raise a message of error when there are too many differences wanted (to change with proper error message!)
if Number_values_to_change <= Number_of_neurons:
    to_change = np.random.randint(0, Number_of_neurons, size=Number_values_to_change)
    pattern3_new = pattern3.copy()

    for i in to_change:
        if pattern3_new[i] == -1:
            pattern3_new[i] = 1
        else:
            pattern3_new[i] = -1

else:
    print("Too many differences wanted, the initial pattern hasn't enough features to change")

# test of the new random pattern
affiche = bool(0)
if affiche:
    if Number_values_to_change <= Number_of_neurons:
        for j in range(Number_of_neurons):
            if pattern3[j] != pattern3_new[j]:
                print(pattern3[j], pattern3_new[j])


def binary_rule(x):
    if x < 0:
        return -1
    else:
        return 1


def update_rule(pattern_t):
    newmatrix = np.dot(WeightMatrix, pattern_t)
    pattern_t_1 = np.zeros_like(pattern_t)
    for index in range(newmatrix.shape[0]):
        pattern_t_1[i] = binary_rule(newmatrix[i])

    return pattern_t_1


intermediate_state = []

T = 0
pattern_t = np.zeros_like(pattern3_new)

while (pattern_t != pattern3).any() and T < 20:
    pattern_t_1 = update_rule(pattern3_new)
    pattern_t = pattern_t_1.copy()
    intermediate_state.append(pattern_t)
    T += 1
print(T)

print(intermediate_state)
