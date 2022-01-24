stack = []
def push():
    if len(stack) == n:
        print("list is full")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(stack)

def pop():      #LIFO or FILO order
    if not stack:
        print("Stack is full")
    else:
        e = stack.pop()
        print("removed element: ",e)
        print(stack)

n = int(input("Enter limit of stack: "))

while True:
    choice = int(input("Enter a choice 1.push 2.pop 3.quit \n"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Enter a choice 1 or 2 or 3")


