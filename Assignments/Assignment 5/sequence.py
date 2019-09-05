#Takes input n and generates the first n numbers of a formula that starts at one and then adds the three latest numbers
#together to create a new number, starts by adding the available numbers e.g. 1, 1+1=2, 1+2=3

n = int(input("Enter the length of the sequence: ")) # Do not change this line
#define the starting numbers, first number is given the value 1 to so the first addition in for loop will come out correctly
first_number = 1
second_number = 0
third_number = 1
sum_numbers=1

for i in range(0,n):
    print(sum_numbers,end = ', ')
    sum_numbers = first_number + second_number + third_number
    #move the numbers to the right with the sum as the new end number
    first_number = second_number
    second_number = third_number
    third_number = sum_numbers
    
