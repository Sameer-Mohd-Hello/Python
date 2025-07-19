stk = []
while True:
    b = int(
        input(
            """Enter operation to perform :- 
                1.Push in stack
                2.Pop in stack
                3.Peek in stack
                4.Display stack
                5.Exit
                
                """
        )
    )
    if b == 1:
        stk.append(int(input("Enter element :- ")))
        print(stk)
        print()
    elif b == 2:
        if len(stk) == 0:
            print("Stack is empty cannot pop")
            print()
        else:
            print("Element poped :", stk.pop())
            print()
    elif b == 3:
        if len(stk) == 0:
            print("Stack is empty cannot pop")
            print()
        else:
            print("Last element in stack is :", stk[-1])
            print()
    elif b == 4:
        print(stk)
        print()
    elif b == 5:
        print("Exiting program.....")
        break
    else:
        print("invalid choice! try again")
        print()
