stk = []
while True:
    b = int(
        input(
            """Enter operation to perform :- 
                1.Enqueue
                2.Dequeue
                3.Front of queue
                4.Rear of queue
                5.Display
                6.Exit
                
                """
        )
    )
    if b == 1:
        stk.append(int(input("Enter element :- ")))
        print(stk)
        print()
    elif b == 2:
        if len(stk) == 0:
            print("Queue is empty cannot delete")
            print()
        else:
            print("Element removed :", stk.pop(0))
            print()
    elif b == 3:
        if len(stk) == 0:
            print("Queue is empty")
        else:
            print("Front of the queue is :", stk[0])
            print()
    elif b == 4:
        if not stk:
            print("Queue is empty")
        else:
            print("Back of queue is :", stk[-1])
            print()
    elif b == 5:
        print(stk)
        print()
    elif b == 6:
        print("Exiting program.....")
        break
    else:
        print("invalid choice! try again")
        print()
