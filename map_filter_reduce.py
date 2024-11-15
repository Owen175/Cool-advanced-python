def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
value = list(map(multiply, list(range(10))))
print(value)
# Returns 0, 1, 4, 9, 16, ... 

for i in range(5):
    value = list(map(multiply, list(range(10))))
    # Returns 0, 1, 4, 9, 16, ... 
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]



product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24
