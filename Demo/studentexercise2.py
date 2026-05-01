def pattern(n):
    if n == 1:
        print("*")
        return

    pattern(n - 1)   

    print("* " * n)  


pattern(4)