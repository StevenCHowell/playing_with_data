import math
from typing import List, Tuple, Callable

Vector = List[float]
Matrix = List[List[float]]

def add(v: Vector, w: Vector) -> Vector:
    """Add corresponding elements"""
    assert len(v) == len(w), "cannot add vectors of different lengths"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtract corresponding elements"""
    assert len(v) == len(w), "cannot subtract vectors of different lengths"
    return [v_i - w_i for v_i, w_i in zip(v, w)]
    
    
def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    assert vectors, "no vectors provided!"
    
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"
    
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply every element by c"""
    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    num_vectors = len(vectors)
    return scalar_multiply(1/num_vectors, vector_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "cannot calculate product between vectors of different lengths"
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])


def sum_of_squares(v: Vector) -> float:
    """Return v_1 * v_1 + v_2 * v_2 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """Returs the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))


# def distance1(v: Vector, w: Vector) -> float:
#     """Computes the distance between two points, defined by vectors v and w"""
#     return math.sqrt(squared_distance(v, w))


def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between two points, defined by vectors v and w"""
    return magnitude(subtract(v, w))


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
    """Returs the i-th row of the matrix A"""
    return A[i]


def get_col(A: Matrix, j: int) -> Vector:
    """Returs the j-th column of the matrix A"""
    return [row[j] for row in A]


def make_matrix(
    num_rows: int,
    num_cols: int,
    entry_fn: Callable[[int, int], float]
) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i, j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Returns the nxn identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

