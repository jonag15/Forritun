#https://github.com/jonag15/Forritun
#find the maximum positive integer input until a negative value is entered

num_int = int(input("Input a number: "))    # Do not change this line

max_int = num_int
#compare new input to original and keep track of highest number
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line