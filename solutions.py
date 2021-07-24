import numpy

def question1():
    # Write a python program that creates a 5X2 integer array from a range between 100 to
    # 200 such that the difference between each element is 10.

    print("This is will create a 5x2 integer array as given in the question...")
    array = numpy.arange(100, 200, 10)
    reshaped_array = array.reshape(5,2)
    print (reshaped_array)

def question2():
    # Write a python program that returns array of odd rows and even columns from below
    # numpy array
    # sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36],
    # [39 ,42, 45, 48], [51 ,54, 57, 60]]).

    array_given = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
    [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]]) 
    print("Printing Input Array")
    print(array_given)

    print("\n Printing array of odd rows and even columns")
    newArray = array_given[::2, 1::2]
    print(newArray)

def question4():
    # Write a python program that deletes the second column from the given sampleArray and
    # insert the following new column in its place.
    # sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
    # newColumn = numpy.array([[10,10,10]])

    # the original array
    print("Original array")
    sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
    print (sampleArray)

    # the array when the second column is deleted
    print("Array after deleting column 2 on axis 1")
    sampleArray = numpy.delete(sampleArray , 1, axis = 1) 
    print (sampleArray)

    newColumn = numpy.array([[10,10,10]])

    # inserting into column 2
    print("Array after inserting column 2 on axis 1")
    sampleArray = numpy.insert(sampleArray , 1, newColumn, axis = 1) 
    print (sampleArray)

# calling the functions
print()
print('Solving question 1...')
question1()

print()
print('Solving question 2...')
question2()

print()
print('Solving question 4...')
question4()