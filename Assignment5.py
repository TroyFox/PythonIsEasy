"""
Homework Assignment #5: Basic Loops


Details:
 
You're about to do an assignment called "Fizz Buzz", which is one of the classic programming challenges. It is a favorite for interviewers, 
and a shocking number of job-applicants can't get it right. But you won't be one of those people. Here are the rules for the assignment 
(as specified by Imran Gory):

Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".

The one hint you'll likely need is: 

There is a Python operator called "modulo", represented by the percentage sign (%) that gives you the remainder left over after division. 


Extra Credit:

Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime". You should print this whenever you encounter 
a number that is prime (divisible only by itself and one). As you implement this, don't worry about the efficiency of the algorithm you use to 
check for primes. It's okay for it to be slow.


Submitted by: Jansen Gomez
"""
# Function to check for prime number 
def PrimeCheck(number):
    
    if number > 1:
        ctr = 2
        factors = 0
        while(ctr <= number):
            if (number % ctr == 0 and ctr != number):
                factors += 1
            if ctr == number and factors == 0:
                print (number, "- prime" )
                return True

            ctr += 1
        return False

# Main 
for num in range(1,101):

    isPrime = PrimeCheck(num)

    if isPrime == True:
        continue
  
    # for multiples of both 3 and 5 print "FizzBuzz"
    if num % 3 == 0 and num % 5 == 0: 
        print ("FizzBuzz")
    
    # for multiples of 3 only print "Fizz"
    elif num % 3 == 0:
        print ("Fizz")

    # for multiples of 5 only print "Buzz"
    elif num % 5 == 0:
        print ("Buzz")

    # Otherwise print the number
    else:
        print(num)

