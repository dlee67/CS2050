import Stack

r_stack = Stack()

def to_str(n, base):

    conver_string = "0123456789ABCDEF"

    while n > 0:

        if n < base:

            r__stack.push(convert_string[n])

        else:

            r_stack.push(convert_string[n % base])

        n = n // base

    res = ""

    while not r_stack.is_empty():

        res = res + str(r_stack.pop())

    return res

print(to_str(1453, 16))
