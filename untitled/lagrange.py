import numpy


class Lagrange:

    @staticmethod
    def solve(A, B, C, D):
        left_matrix = numpy.array([[2, 0, 0, A], [0, 2, 0, B], [0, 0, 2, C], [A, B, C, 0]])
        right_matrix = numpy.array([0, 0, 0, -D])

        print numpy.linalg.det(left_matrix)

        return numpy.linalg.solve(left_matrix, right_matrix)
