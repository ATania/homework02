import types
import random
import sys
import pytest
import numpy as np
try:
    import matrix
except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'matrix.py'!"


def imports_of_your_file():
    for name, val in vars(matrix).items():
        if isinstance(val, types.ModuleType): #get direct imports
            yield val.__name__#, name
        else: #gets from x import y (and yields the x!)
            imprt = getattr(matrix, name)
            if hasattr(imprt, "__module__") and not str(imprt.__module__).startswith("_") and not str(imprt.__module__) == "matrix":
                yield imprt.__module__


def test_imports():
    allowed_imports = {"copy"}
    assert set(imports_of_your_file()) <= allowed_imports, "You are not allowed to import other modules in this exercise!"
    assert hasattr(matrix, "Matrix"), "Your file has to have a Matrix-class!"


def test_assertions_for_creation_with_constructor():
    with pytest.raises(AssertionError):
        matrix.Matrix([[1, 2, 3], [1, 2], [1, 2, 3]]) #Your class is supposed to assert that the Matrix is not ill-shaped!

    with pytest.raises(AssertionError):
        matrix.Matrix([[1, 2, 3], [1, 2, 'platypus'], [1, 2, 3]]) #Your class is supposed to assert that it can only be constructed with ints or floats

    matrix.Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])


def test_creation_and_string_generation():
    a = matrix.Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 9]])
    assert str(a) == "[[1, 2, 3],\n [4, 5, 6],\n [1, 2, 9]]", "The string-representation of Your Matrix must correspond precisely to what the task said!"
    b = matrix.Matrix.filled(rows=2, cols=4, value=4)
    assert str(b) == "[[4, 4, 4, 4],\n [4, 4, 4, 4]]", "Creating your Matrix with the static filled()-method did not work!"



def generate_random_2dlist(forced_rows=False, forced_cols=False):
    num_rows = random.randint(1, 10) if not forced_rows else forced_rows
    num_cols = random.randint(1, 10) if not forced_cols else forced_cols
    the_data = []
    for i in range(num_rows):
        the_row = []
        for j in range(num_cols):
            the_row.append(random.randint(-999, 999))
        the_data.append(the_row)
    return the_data, num_rows, num_cols


def test_data_method_returns_a_copy():
    #trying a few possibilities...:
    for _ in range(20):
        the_data = generate_random_2dlist()[0]
        a = matrix.Matrix(the_data)
        assert a.data == the_data, "Your data needs a data-property, that returns a list of lists, looking exactly like the one used to create it!"
    #testing if its actually a copy...
    a = matrix.Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 9]])
    assert a.data == [[1, 2, 3], [4, 5, 6], [1, 2, 9]], "Your data needs a data-property, that returns a list of lists, looking exactly like the one used to create it!"

    with pytest.raises(AttributeError):
        a.data = [[1, 2, 3], [1, 2, 3]] #This should raise an AttributeError, because you aren't allowed to set the data!

    internal = a.data
    internal[0][0] = 42
    assert a.data == [[1, 2, 3], [4, 5, 6], [1, 2, 9]], "When you copy the internal data and change the copy, the original data is supposed to stay equal!"


def test_getters_and_setters():
    a = matrix.Matrix([[-1, -2], [-3, -4]])
    # this is the same as assert a[0,0] == -1, only the error will be more informative
    assert a.__getitem__([0, 0]) == -1, "Your setter-method (indexing with comma-separated values in square brackets) didn't return the value it should!"

    a[0, 0] = 42
    assert a[0, 0] == 42, "Your setter-method (indexing with comma-separated values in square brackets) didn't correctly set the value!"
    assert a.data[0][0] == 42, "Your setter-method (indexing with comma-separated values in square brackets) didn't correctly set the value!"

    for _ in range(20):
        the_data, nrows, ncols = generate_random_2dlist()
        a = matrix.Matrix(the_data)
        row = random.randint(0, nrows-1)
        col = random.randint(0, ncols-1)
        # this is the same as assert a[row, col] == a.data[row][col], only the error will be more informative
        assert a.__getitem__([row, col]) == a.data[row][col], "Your getter-method (indexing with comma-separated values in square brackets) didn't return the value it should!"

        random_val = random.randint(-99, 99)
        a[row, col] = random_val
        assert a[row, col] == random_val, "Your setter-method (indexing with comma-separated values in square brackets) didn't correctly set the value!"
        assert a.data[row][col] == random_val, "Your setter-method (indexing with comma-separated values in square brackets) didn't correctly set the value!"


def test_matrix_transpose():
    a = matrix.Matrix([[-1, -2], [-3, -4]])
    b = a.T
    assert isinstance(b, matrix.Matrix), "Your transposed Matrix is supposed to be a matrix as well!"
    assert b.data == [[-1, -3], [-2, -4]], "You transposed your Matrix wrongly!"
    assert str(b) == "[[-1, -3],\n [-2, -4]]", "You transposed your Matrix wrongly!"
    assert str(a) == "[[-1, -2],\n [-3, -4]]", "You changed the original Matrix when transposing!"
    a[0, 0] = 42
    b[1, 1] = 1337
    assert a.data == [[42, -2], [-3, -4]], "Changing the transposed Matrix changed the original one!"
    assert b.data == [[-1, -3], [-2, 1337]], "Changing the original Matrix changed the transposed one!"


def test_matrix_addition():
    a = matrix.Matrix([[-1, -2], [-3, -4]])
    b = matrix.Matrix.filled(rows=2, cols=2, value=4)
    c = a + b
    assert isinstance(c, matrix.Matrix), "The result of the addition must be a Matrix as well!"
    assert c.data == [[3, 2],[1, 0]], "The result of your addition is not correct!"

    a2 = matrix.Matrix([[-1, -2], [-3, -4]])
    b2 = matrix.Matrix([[-1, -2], [-3, -4]])
    assert (a+b).data == [[3, 2],[1, 0]], "The result of your addition is not correct!"


def test_scalar_multiplication():
    a = matrix.Matrix.filled(rows=2, cols=2, value=4)
    b = 5 * a
    assert isinstance(b, matrix.Matrix), "The product must be a Matrix as well!"
    assert b.data == [[20, 20], [20, 20]], "The product is not correct!"

    a2 = matrix.Matrix([[-1, -2], [-3, -4]])
    c2 = 3.1415 * a2
    assert c2.data == [[-3.1415, -6.283], [-9.4245, -12.566]], "The product is not correct!"


def test_matrix_multiplication():
    a = matrix.Matrix([[-1, 4, -2]])
    b = matrix.Matrix([[1], [2], [3]])
    c = a * b
    d = b * a
    assert isinstance(c, matrix.Matrix), "The product must be a Matrix as well!"
    assert c.data == [[1]], "The product is not correct!"
    assert d.data == [[-1, 4, -2], [-2, 8, -4], [-3, 12, -6]], "The product is not correct!"


def test_matrix_multiplication_with_numpy_comparision():
    for _ in range(20):
        #this will create a matrix, a second one with the same number of rows, and a third one with the same number of cols
        firstlist = generate_random_2dlist()
        firstmatrix = firstlist[0]
        secondmatrix = generate_random_2dlist(forced_cols=firstlist[1])[0]
        thirdmatrix = generate_random_2dlist(forced_rows=firstlist[2])[0]

        #in numpy, matrix multiplicaiton is numpy.dot(matrix1, matrix2). This should correspond to your solution.
        numpy_first = np.dot(np.array(secondmatrix), np.array(firstmatrix))
        own_first = matrix.Matrix(secondmatrix)*matrix.Matrix(firstmatrix)
        numpy_second = np.dot(np.array(firstmatrix), np.array(thirdmatrix))
        own_second = matrix.Matrix(firstmatrix)*matrix.Matrix(thirdmatrix)

        assert numpy_first.tolist() == own_first.data, "For some data, your solution does not correspond to the Numpy-Solution!"
        assert numpy_second.tolist() == own_second.data, "For some data, your solution does not correspond to the Numpy-Solution!"




if __name__ == "__main__":
    pass
