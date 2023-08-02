# List comprehensions examples [P356]

# Matrix
matrix = [[i, j] for i in range(0, 3)
                 for j in range(0, 3)]

position = [[i, j, ((4 * i) + j)] for i in range(0, 4)
                                  for j in range(0, 4)]


# Calculations
even = [i for i in range(0, 15) if (i % 2 == 0)]
odd = [i for i in range(0, 15) if (i % 2 != 0)]

square = [(i ** 2) for i in range(0, 10)]


# Filter
index = [i for (_, _, i) in position]



