print(
    """Enter choice of operation
      1: ADD
      2: SUB
      3: MULTIPLY
      4: DIVIDE
      5: EXIT"""
)
a = int(input("enter choice: "))
if a == 5:
    print("Thankyou for using calculator")
elif a in [1, 2, 3, 4]:
    m = int(input("enter val1: "))
    n = int(input("enter val2: "))
    if a == 1:
        print(abs(m + n))
    elif a == 2:
        print(abs(m - n))
    elif a == 3:
        print(abs(m * n))
    elif a == 4:
        if n == 0:
            print("cannot divide by zero")
        else:
            print(abs(m / n))
