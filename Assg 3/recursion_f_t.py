def main():

#They want me to pass the argument 5 to the message
#so it will act as a maximum depth of recursion.

    message(5)

def message(times):

    if times > 0:

        print('This is a recursive function.')

        message(times - 1)

main()

