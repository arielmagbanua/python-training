def averages(grades):
    """
    (list of list of number) -> list of float

    Return a new list in which each item is the average of the
    grades in the inner list at the corresponding position of
    grades.

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    """

    average_list = []

    for grades_list in grades:
        # Calculate the average of grades_list and append it
        # to average_list.

        total = 0
        for mark in grades_list:
            total = total + mark

        average_list.append(total / len(grades_list))

    return average_list
