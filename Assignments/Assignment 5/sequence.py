#Takes input n and generates the first n numbers of a formula that starts at one and then adds the three latest numbers
#together to create a new number, starts by adding the available numbers e.g. 1, 1+1=2, 1+2=3

n = int(input("Enter the length of the sequence: ")) # Do not change this line
#define the starting numbers
first_number = 0
second_number = 0
third_number = 1

for i in range(0,n):
    #The first move to the right gives the wrong end number (0,1,1 insted of 0,1,2) so a special case is made for the first move
    if i <1:
        sum_numbers = first_number + second_number + third_number
        print(sum_numbers,end = ', ')
    
        #move the numbers to the right and add 2 as the end number
        first_number = second_number
        second_number = third_number
        third_number = 2
        continue
    #the rest of the loop goes on as normal
    sum_numbers = first_number + second_number + third_number
    print(sum_numbers,end = ', ')
    
    #move the numbers to the right with the sum as the new end number
    first_number = second_number
    second_number = third_number
    third_number = sum_numbers
    
