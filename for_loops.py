

# 9. Write a program that checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not. (+15 points)

# 10. Write a program that prints out the prime numbers less than 1000. (+20 points)



print("Options: 1,2,3,4,5,6,7,8,9,10")
run = input("Enter the problem you want to run:")
run =int(run)



# Program 1 (a program that prints out the numbers 1 to 1000)



if run == 1:
    print("Running problem 1")
    for count in range(1, 1001):
        print(count)



# Program 2 (a program that prints out the odd numbers between 1 and 1000)



elif run == 2:
    print("Running problem 2")
    for count in range(1, 1001, 2):
        print(count)



# Program 3 (a program that prints out the numbers between 0 and 1000 that are divisible by 3)   
        


elif run == 3:
    print("Running problem 3")
    for num in range(1,1000):
        if num % 3 == 0:
            print(num)
        else:
            pass    



# Problem 4 (a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5)
        


elif run == 4:
    print("Running problem 4")
    for num in range(1,1000):
        if num % 3 == 0:
            print(num)
        elif num % 5 == 0:
            print(num)
        else:
            pass
    


 # Problem 5 (a program that asks the user to enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200. (+10 points) Extra credit if the programs asks again if the number is less than 200)



# elif run == 5:
#     print("Running problem 5")
#     num = int(input("Enter a number greater than 200: "))
#     for count in range(0, 200): 
#         num = int(input("Would you like to try again? Please enter a number greater than 200 "))
#         for num in range(201, num):
#                 if num % 11 == 0:
#                     print(num)
#                 elif num % 13 == 0:  
#                     print(num)  
                


elif run == 5:
    print("Running problem 5")
    num = int(input("Enter a number greater than 200: "))
    for count in range(0, 200): 
            num = int(input("Would you like to try again? Please enter a number greater than 200 "))
            if num > 200:
                break
    for num in range(1, num):
                if num % 11 == 0:
                    print(num)
                elif num % 13 == 0:  
                    print(num)  



 # Problem 6 (a program that prints out each letter of a string line by line)



elif run == 6:
    print("Running problem 6")
    line_by_line = str(input("Enter a string: "))
    for l in range(len(line_by_line)):
            print(line_by_line[l])



# Problem 7 (a program that asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long)



elif run == 7:
    print("Running problem 7")

    line_by_line = input("Enter a string: ")
    for l in range(10):
        if len(line_by_line) < 10:
            line_by_line = input("The string must be more than 10 letters long")
    # for l in range(len(line_by_line)):
    # for l in range(len(line_by_line[::2])):
    for l in range(0, len(line_by_line), 2):
        print(line_by_line[l])



# Problem 8 
        
elif run == 8:
    print("Running problem 8")


    import random
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0

    for rolls in range (1000): 
        dice = random.randint(1,6)
        if (dice ==1):
            ones += 1
        elif dice == 2:
            twos += 1
        elif dice == 3:
            threes += 1
        elif dice == 4:
            fours += 1
        elif dice == 5:
            fives += 1
        elif dice == 6:
            sixes += 1
    for l in range(1,7):
        print(f"#{l} was rolled {ones} times ")
        print(f"#{2} was rolled {twos} times")
        print(f"#{3} was rolled {threes} times")
        print(f"#{4} was rolled {fours} times ")
        print(f"#{5} was rolled {fives} times ")
        print(f"#{6} was rolled {sixes} times")
    

