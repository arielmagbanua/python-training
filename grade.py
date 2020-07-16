import tkinter.filedialog

def read_grades(gradefile):
    '''(file open for reading) -> list of float

    Read and return list of grades in the gradefile.

    Precondition: gradefile starts with a header that contains
    no blank lines, then has a blank line, and then lines
    containing a student number and a grade.
    '''

    # skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    # Read the grades. accumulating them into a list.

    grades = []

    line = gradefile.readline()
    while line != '':
        # now we have s string containing the info for a
        # single student.
        # Find the last space and take everything after that
        # space.
        grade = line[line.rfind(' ')+1:]
        grades.append(float(grade))
        line = gradefile.readline()

    return grades

def count_grade_ragnes(grades):
    '''(list if float) -> list of int

    Return a list of int where each index indicates how many grades were in these
    ranges:

    0-9: index 0
    10-19: index 1
    20-29: index 2
      .
      .
    40-49: index 9
    50-59: index 10

    >>> grade_ranges([77.5, 37.5, 0.5, 9.5, 72.5, 100.0, 55.0, 70.0, 79.5])
    [2, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]
    '''

    range_counts = [0] * 11

    for grade in grades:
        which_range = int(grade // 10)
        range_counts[which_range] = range_counts[which_range] + 1
    
    return range_counts

def write_histogram(range_counts, histfile):
    '''(list of int, file open for writing) -> NoneType

    Write histogram of *'s base on the number of grades in each range.

    The output format:
    0-9: *
    10-19: **
    20-29: *****
      .
      .
    40-49: **
    50-59: *
    '''

    histfile.write('0-9:   ')
    histfile.write('*' * range_counts[0])
    histfile.write('\n')

    # Write the 2-digit ranges.
    for i in range(1, 10):
        low = i * 10
        high = i * 10 + 9
        histfile.write(str(low) + '-' + str(high) + ': ')
        histfile.write('*' * range_counts[i])
        histfile.write('\n')

    histfile.write('100:   ')
    histfile.write('*' * range_counts[-1])
    histfile.write('\n')

