#program taking users name and age as input and prints a greeting message
#QUIZ 2222222
name=input("Enter your name: ")
ages =int(input("Enter your age: "))
print("hy %s, are you %d years old" % (name, ages))
#
##Quiz 4444444
#FIND MA AND MINIMUM VALUE GIVEN  A LIST OF NUMBERS
numbers = [2, 54, 7, 10, -3]
max_value = max(numbers)
min_value = min(numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

####QUIZ 88888888
#find sum of all positives given a list of intergers
my_list = [2, 5, 8, -2, 4]
result = sum([x for x in my_list if x > 0])
print("the sum of positive numbers is:", result)
##QUIZ 1010101
x = 10
y = 5
temp = x  # Store the value of x in a temporary variable
x = y     # Assign the value of y to x
y = temp   # Assign the original value of x (stored in temp) to y
print("After swapping: x =", x)
print("After swapping: y =", y)