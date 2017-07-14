#practicing recursion.

def main():

    number = int(input('Enter a nonnegative integer: '))

    #Start of the recursion
    fact = factorial(number)

    #Display the factorial.
    print('The factorial of', number, 'is', fact)

# The factorial functions uses recursion
#to make factorial
#

def factorial(num):

    if num == 0:

        return 1

    else:

        return num * factorial(num - 1)

#main function being called.
main()
        
#So, it's returning an expression, but that expression will perform recursion.

#The book says it does not immidiately return.

#The value for the factorial(num - 1) must be determind.

#In my understanding at least, each time the return is triggerd,
#
#a value that is being timed with num will be returned;
#
#then, fact will store the value and stu...
#
#I need a full fledged white board interaction.
#
#really.
    
