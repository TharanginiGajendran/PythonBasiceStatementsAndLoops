
# if statement inside another if statement is called nested if statement
# syntax
# if condition1:
#    executes when condition1 is true
#     if condition2:
#         executes when condition2 is true
# statement outside if block


x = 10
if x < 50:
    if x > 10:
        print("x is equal to 10")
    # the below line belongs to first if condition
    # it prints regardless of if the 2nd condition is not satisfied
    print("x is less than 50")
print("*********End**********")
