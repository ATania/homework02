# Homework 02

## Starting the environment

Before you start, don't forget to enable your conda environment using

    source activate scientific

on Unix-based systems, or

    activate scientific

on Windows. If you named your environment differently, you can figure out its
name by running the command

    conda info --envs

After you activated your environment, make sure to install all requirements of
this current week by changing to your project-folder and running

    pip install -r requirements.txt


## Your task

Your task this week is to write a *Matrix* class that simulates a mathematical 2D-matrix and can be used to do basic matrix operations. The name of your matrix-class is supposed to be **Matrix**, and it is supposed to be in a file *matrix.py*. Your class has to fulfill all the use-cases mentioned below, and besides the `copy`-module, you are not allowed to use additional libraries!

The matrix should contain only numerical data (ints and floats). For now, you can simply use an `assert`-statement to check for that. Furthermore, when constructing the Matrix, you have to make sure that all lines are of the same length, you can again do that with an assertion. As we didn't get to exceptions yet, you don't have to handle any other error-scenarios except the ones mentioned here.

### Hints
You will need a magic method that was not mentioned in class, namely `__rmul__()`. You are supposed to inform yourself about its usage on the internet. Further, you may want to look up `__getitem__()` and `__setitem__()`

### Use cases

1. **Creation** -  In general there are two resonable ways of how to create a new
matrix. Either you have the complete data already, or you want to use a
single value to create a matrix for a given shape. For the first way to create a matrix, the following code should work as expected:
```python
# create a matrix with data being [[1, 2], [3, 4]]
a = Matrix([[1, 2], [3, 4]])
```
Specific creation procedures like the second one are usually realized with static functions
inside of the class - to realize that, the second way to create a Matrix should look something like this:
```python
# create a matrix filled with zeros with 2 rows and 3 columns
b = Matrix.filled(rows=2, cols=3, value=0)
# this should have the values: #[[0, 0, 0], [0, 0, 0]]
```

2.  **Printing** - Make sure that your matrix can be printed with nice formatting
for debugging and such with python’s built-in print-function, like:
```python
a = matrix.Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 9]])
print(a)
#The result should look like this:
#[[1, 2, 3],
# [4, 5, 6],
# [1, 2, 9]]
```

3. **Data readout** - There should be a way to get all the data stored in the
matrix in nested lists format. Make sure that the internal data cannot be
modified in this way! This includes making sure that this only gives a copy
of the internal data.
```python
a = Matrix([[1, 2], [3, 4]])
print(a.data == [[1, 2], [3, 4]])
# should return true
#
# this must not work:
a.data = [[0, 0], [0, 0]]
#
# also careful with copying!
internal = a.data
internal[0][0] = 42
print(a.data == [[1, 2], [3, 4]])
# should still be true
```

4. **Access and modify values** - Normally the square brackets `[]` are used to
access and modify values in containers. Your matrix should also support
that. A 2D-list can be accessed with e.g. `mylist[0][0]`. For the matrix
the following will be even nicer:
```python
a = Matrix([[1, 2], [3, 4]])
print(a[0, 0])
# should print "1"
#
print(a[1, 0])
# should print "3"
#
# modify
a[0, 1] = 42
print(a.data == [[1, 42], [3, 4]])
# should be true
```

5. **Matrix transpose** - Your Matrix-class is supposed to have a property Matrix.T, which returns the transpose of the Matrix, while leaving the original one untouched. Creating the transpose can be done with a single line of code, using a command we had in class.
```python
a = Matrix([[1, 2], [3, 4]])
b = a.T
#
print(isinstance(b, Matrix))
print(b.data == [[1, 3], [2, 4]])
# should both be true
#
# again make sure that you copy the data
a[0, 0] = 42
print(b.data == [[1, 3], [2, 4]])
# should still be true
```

6. **Matrix addition** - Adding two matrices with same shape should give the
correct result. Note that for this task, you can simply assume that both matrices have identical dimensions.
```python
a = Matrix([[1, 2], [3, 4]])
b = Matrix.filled(2, 2, 1)
c = a + b
#
print(isinstance(c, Matrix))
print(c.data == [[2, 3], [4, 5]])
# should both be true
```

7. **Scalar multiplication** - Implement scalar multiplication that works with ints and floats. It is enough if you only consider cases where the Matrix is the second factor:
```python
a = Matrix([[1, 2], [3, 4]])
b = 2 * a
#
print(isinstance(b, Matrix))
print(b.data == [[2, 4], [6, 8]])
# should be true
```

8. **Matrix multiplication** - Implement matrix multiplication that works for
matrices with the correct shape (without error-handling if they aren't and without error-handling if the seonc one even is a Matrix). If you are unsure how matrix multiplication works, the internet will provide a great help ;)
```python
a = Matrix([[1, 2]])
b = Matrix([[3], [4]])
# multiply, different orders
c = a * b
d = b * a
# expected results:
print(isinstance(c, Matrix)) # true
print(isinstance(d, Matrix)) # true
print(c.data == [[11]]) # true
print(d.data == [[3, 6], [4, 8]]) # true
```



> Good luck!
