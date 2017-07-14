def tree(branch_len, t):

    if branch_len > 5:

        t.forward(branch_len)

        t.right(20)

        tree(branch_len - 15, t)

        t.left(40)

        tree(branch_len - 10, t)

        t.right(20)

        t.backward(branch_len)
