def recur(num, count):

    if num > 1:

        print("level %d :: F, count %d " % (num, count))

        count = recur(num - 1, count + 1)

        print("Level %d :: S, count %d " % (num, count))

        counnt = recur(num - 1, count + 1)

        return count

    else:

        print("level %d :: L, count %d" % (num, count))

        return count + 1

recur(5,0)
