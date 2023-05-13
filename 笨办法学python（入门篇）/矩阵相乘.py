# class Matrix:
#     def __init__(self, *args):
#         self.rows = len(args)
#         self.cols = len(args[0])
#         self.data = []
    
#     def __str__(self):
#         return "Matrix:\n" + "\n".join([" ".join([str(x) for x in row]) for row in self.data])
    
#     def __mul__(self, other):
#         new_data = []
#         for i in range(self.rows):
#             new_row = []
#             for j in range(other.cols):
#                 new_value = sum([self.data[i][k] * other.data[k][j] for k in range(self.cols)])
#                 new_row.append(new_value)
#             new_data.append(new_row)
#         return Matrix(*new_data)
    
# matrix1 = Matrix([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
# matrix2 = Matrix([1, 2], [3, 4], [5, 6], [7, 8])
# print(matrix1 * matrix2)

# answer
class Matrix:
    def __init__(self, *args):
        self.data = list(args)
        self.rows = len(args)
        self.cols = len(args[0])
        if any(len(row) != self.cols for row in self.data):
            raise ValueError("All rows must have the same length")

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions not compatible for multiplication")
        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(other.cols):
                new_value = sum([self.data[i][k] * other.data[k][j] for k in range(self.cols)])
                new_row.append(new_value)
            new_data.append(new_row)
        return Matrix(*new_data)

matrix1 = Matrix([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
matrix2 = Matrix([1, 2], [3, 4], [5, 6], [7, 8])
matrix3 = matrix1 * matrix2
print(matrix3)
