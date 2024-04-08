def generator():
    x = 1
    while x < 20:
        yield x
        x += 1


print(next(generator()))
