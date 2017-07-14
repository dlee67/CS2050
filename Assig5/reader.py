file_obj = open("highways.txt")

while file_obj:

    read = file_obj.read()

    print(read)

    if read == ' ':

        break
