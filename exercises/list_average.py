# input numeric grades in a list sequence
grades = [int(num) for num in input().split()]

# initialized failing grades to 0
failing_grades = 0

# counting of failing grades
for grade in grades:
    if grade < 72:
        failing_grades += 1

# get the sum of all grades
sum_of_grades = sum(grades)

# get the number of grades inputed
len_of_grades = len(grades)

# getting the average of the numeric grades
average = sum_of_grades / len_of_grades
float_average = float(average)

# print the output
if failing_grades == 0:
    print(f"Average is: {float_average:.2f}. You didn't fail in any subject.")
elif failing_grades == len_of_grades:
    print(f"Average is: {float_average:.2f}. You failed in all your subjects.")
else:
    print(f"Average is: {float_average:.2f}. You failed in {failing_grades} subjects.")
