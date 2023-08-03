# List comprehensions examples [P356]

# Matrix
matrix1 = [[i, j] for i in range(0, 3)
                  for j in range(0, 3)]

matrix2 = [[i for i in range(0, 3)] for j in range(0, 3)]

position = [[i, j, ((4 * i) + j)] for i in range(0, 4)
                                  for j in range(0, 4)]


# Calculations
even = [i for i in range(0, 15) if (i % 2 == 0)]
odd = [i for i in range(0, 15) if (i % 2 != 0)]

square = [(i ** 2) for i in range(0, 10)]


# Filter
index = [i for (_, _, i) in position]


# Function
def square_root(x):
    sqt = x ** (1/2)

    return sqt


sqt_list = [square_root(i) for i in range(1, 6)]

