def triangle():
    for number in range(0, 5):
        total = ""
        for star in range(0, number + 1):
            total += "*"
        print(total)


triangle()
